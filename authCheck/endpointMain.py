# main file for OVC endpoint auth checker
import Endpoint as end 

# TODO this might be a CSV file, tbd. Easy adjustment though either way
def readEndpointFile(configFile):
    '''
    * fxn: readEndpointFile()
    * does: reads in lines (str) from file into list of endpoints (strs)
    * params: 
        - str configFile - file of all the endpoints
    * returns: endPointList, list, list of all endpoints
    '''
    endPointList = []

    with open(configFile) as f:
        for i in f:
            # strips newline in i
            i2 = i[:-1]
            endPointList.append(i2)
    
    return endPointList

def makeEndpointObjects(uris, endpointSuffixes):
    '''
    fxn: makeEndpointObjects()
    does: builds a dict of endpoint objects (see Endpoint.py)
    params:
        - uris: list of cnames for customers 'www.mycustom.com/...'
        - endpointSuffixes: list of endpoint sfx's, '..../my/endpoing/suffix'
    returns: dict of endpoint objects
    '''
    endpointObjs = []
    totalUris = len(uris)
    totalEndpoints = len(endpointSuffixes)

    # o(n*m)
    for i in range(totalUris):
        base = uris[i]
        
        for j in range(totalEndpoints):
            endObj = end.Endpoint(base, endpointSuffixes[j])
            # TODO - how do I want to store these objects?
            endpointObjs.append(endObj)
        


    
    return endpointObjs


def showTests(endObjs):

    num = 0
    for obj in endObjs:
        num += 1
        print("\n\n")
        print("*"*8 + " Test: " + str(num) + "*"*8)
        print("Endpoint: " + obj.uri + "\n" + "Status: " + str(obj.status) +
                "\nPassed: " + str(obj.passed) + '\n'
                + "Grabbed Data: " + str(obj.grabbedheader))


def summarizeReport(endObjs):

    for i in range(len(endObjs)):
        print("\n" + "*"*20)
        print(endObjs[i])



def main():

    # open file, read in URis, return list of endpoints (string)
    # TODO change to sys.argv
    configFile = 'endpointsNYT.txt'
    endpointSuffixes = readEndpointFile(configFile)

    # build endpoint object for each, store in symbol table
    # replace w/ cnames from SEF
    # TODO change to sys.argv - read in file
    baseURI0 = ['www.google.com', 'www.facebook.com']
    baseURI1 = ['www.nytimes.com',]
    endpointOjbects = makeEndpointObjects(baseURI1, endpointSuffixes)

    #for i in endpointOjbects:
    #    print(i.uri)

    testResults = {}
    # run authcheck per endpoint
    for obj in endpointOjbects:
        # runs authcheck
        obj.ping()
    

    showTests(endpointOjbects)

    summarizeReport(endpointOjbects)


    # store ping result in objec





main()