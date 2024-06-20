import docker


def run_container(image: str, environments: dict, ports: dict):
    client = docker.from_env()
    return client.containers.run(image,
                          remove=True,
                          #healthcheck= TODO
                          #log_config= TODO from https://docker-py.readthedocs.io/en/stable/api.html#docker.types.LogConfig
                          detach=True,
                          ports=ports,
                          environment=environments
                          )


# Run example:
# x = run_container("postgres:latest",
#               {'POSTGRES_PASSWORD': 'postgres_pass'},
#               {'5432/tcp': '5432'},
#               )

# Logs gathering - will be useful in the future
# d = x.logs(stream=True)
# try:
#     while True:
#         line = next(d).decode('utf-8')
#         print(line)
# except StopIteration:
#     print("Finished collecting logs")
