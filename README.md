# Development

For development purposes you will need to install the python environment and dependencies.

    virtualenv -p python3.6 venv
    source venv/bin/activate
    pip install -r requirements.txt

Run the rabbitmq container.

    docker run -d -p 5672:5672 rabbitmq:3

Then bring up the nameko service

    nameko run services.foo

You can then interact with the service through the nameko shell.

    nameko shell
    >> n.rpc.foo.square_odd([1, 2, 3, 4, 5])
    >> code = n.rpc.foo.encode(['this is a test string', 'this is another test string'])
    >> n.rpc.decode(code['this is a test string'])

Run the tests using pytest.

    pytest

# Running the service with docker

Build the docker container

    docker build -f Dockerfile . -t foo:latest

Install docker-compose on your system.

    sudo apt install docker-compose

Then bring up the containers.

    docker-compose up -d

Interact with the service through the nameko shell (you will need to install nameko if you haven't already)

    pip install nameko
    nameko shell
    >> n.rpc.foo.square_odd([1, 2, 3, 4, 5])
    >> code = n.rpc.foo.encode(['this is a test string', 'this is another test string'])
    >> n.rpc.decode(code['this is a test string'])

# Notes
