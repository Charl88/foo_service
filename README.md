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

The nameko microservice library seems to work well and provides an easy entry into rpc/pubsub and even http interfacing microservices.

It takes no longer than 10 minutes to scan through the docs in order to learn enough to set up the necessary parts for this task.

The first function (square_odd) was trivial and took 5 minutes to write.

The encoding and decoding of the strings was interesting, as it lead me to read a little about the Huffman compression algorithm, and also about using different serializers in nameko microservices. Spent probably around 15 minutes getting some background info on what this algorithm does and finding a decent python library for it.

At first I tried using the 'pickle' serializer to handle the output from the dahuffman library, but ran into a few issues. The serializer wasn't able to properly handle the output and nameko hangs when serialization fails (see https://github.com/nameko/nameko/issues/658). I spent around 10 minutes playing around with the serialization and trying different things to get it to not hang.

I didn't want to spend too long debugging the serialization, and also re-read the task description which specified that it wanted the output in a string, so I opted to encode the Huffman output to base64 string representation and use the default json serializer. This part took another 10 minutes.

Total time spent on the task was around an hour, including setting up the docker containers, testing everything, and writing up some documentation.
