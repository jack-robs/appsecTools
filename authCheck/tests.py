#tests for appsec - endpoint pinging for auth
import Endpoint
import endpointMain as source


def buildUriTest():

    endpoint = Endpoint.Endpoint('host.com', "/url2")
    if (endpoint.uri == "host.com/url2"):
        return 1
    else:
        return 0

def testFileRead():

    #TODO test could allow validation of endpoint api file - look for typeos etc.
    
    # ensure this is in same directory as tests.py
    testFile = 'endpointTests.txt'
    bumpList = ['test/endpoint', '/test2/endpoint', '//badEndpoint']
    testList =[]

    fromSource =source.readEndpointFile(testFile)

    for i in range(len(fromSource)):
        print(fromSource[i] + ' vs ' + bumpList[i])

    # TODO non-visual test comparison

def testObjectFactory():

    # testing object equality ... interesting testing challenge...

    pass
    
            


def main():

    result = 0
    num = 0

    # test buildUri class method
    result += buildUriTest()
    num += 1
    print(result, result/num)

    testFileRead()




main()
    