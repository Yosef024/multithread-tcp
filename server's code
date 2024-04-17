import socket
import threading
lib={

'Distributed System': 'A system that consists of multiple computers (nodes) that communicate and coordinate their actions to achieve a common goal.',
'Node': 'An individual computer or device participating in a distributed system.',
'Concurrency': 'The ability of a system to handle multiple tasks (processes) seemingly simultaneously.',
'Parallelism': 'The execution of multiple tasks (processes) truly simultaneously using multiple processing units (cores).',
'Transparency': 'The ability of a distributed system to hide the complexity of its internal operations from the user, making it appear like a single, unified system.',
'Scalability': 'The ability of a distributed system to handle increasing workloads or data volumes by adding more nodes.',
'Fault Tolerance': 'The ability of a distributed system to continue operating and providing functionality even if some nodes fail.',
'Load Balancing': 'The process of distributing workload across multiple nodes in a distributed system to optimize resource utilization and performance.',
"Distributed Lock": 'A mechanism used to ensure exclusive access to shared resources in a distributed system, preventing conflicts between nodes.',
'Consistency Model': 'A set of rules that defines how data updates are propagated and maintained across different nodes in a distributed system.' ,
'Replication': 'Copying data to multiple nodes in a distributed system to improve availability and fault tolerance.',
'Message Passing': 'A communication paradigm where nodes exchange messages to communicate and coordinate their actions.',
'Remote Procedure Call (RPC)': 'A mechanism that allows a program on one node to execute code on another node as if it were running locally, hiding the communication details.',
'Distributed Database': 'A database system that stores data across multiple nodes in a distributed system, enabling efficient access and management of large datasets.',
'Middleware': 'Software that sits between applications and distributed system resources, providing services like communication, security, and resource management.',
'Distributed File System': 'A file system that allows storage and access of data across multiple nodes in a distributed system, providing a unified view of files to users.',
'Distributed Hash Table (DHT)': 'A data structure and algorithm for storing and retrieving key-value pairs across a distributed system in a scalable and efficient manner.',
'Consensus Algorithm': 'A protocol used in distributed systems to ensure agreement on a single value among all nodes, even in the presence of failures.',
'Leader Election': 'The process of selecting a single node to act as a leader or coordinator for specific tasks within a distributed system.',
'Distributed Coordination Service': 'A service that provides mechanisms for coordinating activities and managing state across different nodes in a distributed system.',
'Atomicity': 'The property of a transaction in a distributed system that ensures all operations within the transaction either succeed or fail completely.',
'Idempotence': 'The property of an operation in a distributed system that ensures it can be executed multiple times without changing the outcome, preventing unintended consequences.',
'Deadlock': 'A situation where two or more nodes in a distributed system are waiting for resources held by each other, preventing any progress.',
'Livelock': 'A situation where two or more nodes in a distributed system are continuously sending messages back and forth without making progress.',
'Distributed Tracing': 'A technique for tracking the execution path of a request across multiple nodes in a distributed system, aiding in debugging and performance analysis.',
'Microservices': 'An architectural style for building applications as a collection of small, independent services that communicate with each other over well-defined APIs.',
'Container Orchestration': 'The process of managing the lifecycle and deployment of containerized applications across a cluster of machines.',
'Cloud Computing': 'On-demand delivery of IT resources like computing power, storage, and networking over the internet, enabling distributed systems to be built and scaled more easily.',
'API Gateway': 'A single entry point for a distributed system, handling client requests and routing them to the appropriate services.',
'Service Discovery': 'The mechanism used by distributed systems to locate and access services dynamically, allowing nodes to find and communicate with each other efficiently.'}
def search(text):
    if text in lib.keys():
        return lib[text]
    else:
        return 'undefined'
def client(socket2,address):
    inp=socket2.recv(1024).decode()
    out=search(inp)
    socket2.send(out.encode())
    socket2.close()


server_port=30000
server_socket=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
server_socket.bind(('',server_port))
print('start')
server_socket.listen(1)
while True:
    socket2,address=server_socket.accept()
    threading.Thread(target=client,args=(socket2,address)).start()

