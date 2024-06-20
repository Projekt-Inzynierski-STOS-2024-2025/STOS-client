import docker
from docker.models.containers import Container


def run_log_gathering(container: Container) -> None:
    logs = container.logs(stream=True)
    try:
        while True:
            line = next(logs).decode('utf-8')
            print(line)
    except StopIteration:
        print("Finished collecting logs")


def run_container(image: str, environments: dict, ports: dict, healthcheck: dict) -> Container:
    # TODO log_config with https://docker-py.readthedocs.io/en/stable/api.html#docker.types.LogConfig
    client = docker.from_env()
    return client.containers.run(image,
                                 remove=True,
                                 healthcheck=healthcheck,
                                 detach=True,
                                 ports=ports,
                                 environment=environments
                                 )


def run_example():
    db_name: str = "test_db"
    img: str = "postgres:latest"
    envs: dict = {
        'POSTGRES_USER': 'postgres',
        'POSTGRES_PASSWORD': 'admin',
        'POSTGRES_DB': db_name,
        'PGUSER': 'postgres'
    }
    img_ports: dict = {
        '5432/tcp': '5432'
    }
    check = {
        'test': ['CMD-SHELL', 'pg_isready', '-d', db_name],
        'interval': 1_000_000_000 * 3,      # in nanoseconds. Time between healthchecks.
        'timeout': 1_000_000_000 * 10,      # in nanoseconds. Time to consider check as hung.
        'retries': 5,                       # Number of healthchecks before considering service as not working.
        'start_period': 1_000_000_000 * 1   # in nanoseconds. Time to start sending healthchecks.
    }

    container: Container = run_container(img, envs, img_ports, check)
    run_log_gathering(container)


run_example()
