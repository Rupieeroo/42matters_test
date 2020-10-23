# 42 Matters Test - 4
Here is my solution to task 4 of the 42 Matters test.

1.) Convert JSON data from one structure to another

## Structure
I have built an isolated docker container that downloads the dependancies and runs the script.
To build the container:
```
docker build -t apps .
```
Then to run the container:
```
docker run apps
```
The output should list all of the JSON objects one after the other and could take a while to run.

### Dockerfile
The Dockerfile will set up the environment and download the 'jq' dependancy before extracting the file with 'tar'

### Json conversion
calling the 'docker run apps' command will output the JSON objects.

## Conclusion
I had never used 'jq' before so this was a great learning experience I didn't have too much trouble with this but I was stalled for a while attempting the ranking value, as I had to dig into the docs to fully understand what was possible with indexing for the JSON objects.