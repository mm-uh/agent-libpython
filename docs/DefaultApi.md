# lib_agent.DefaultApi

All URIs are relative to *http://agentplatform.grs.uh.cu/api/v1*

Method | HTTP request | Description
------------- | ------------- | -------------
[**get_agent**](DefaultApi.md#get_agent) | **GET** /getAgent/{Name} | 
[**get_agents_by_function**](DefaultApi.md#get_agents_by_function) | **GET** /getAgentsForFunction/{Name} | 
[**get_agents_names**](DefaultApi.md#get_agents_names) | **GET** /getAllAgentsNames | 
[**get_peers**](DefaultApi.md#get_peers) | **GET** /getPeers | 
[**get_similar_agent**](DefaultApi.md#get_similar_agent) | **GET** /getSimilarAgents/{Name} | 
[**register_agent**](DefaultApi.md#register_agent) | **POST** /registerAgent | 


# **get_agent**
> list[Addr] get_agent(name)



Get the agent that follow a simple criteria

### Example

```python
from __future__ import print_function
import time
import lib_agent
from lib_agent.rest import ApiException
from pprint import pprint

# Create an instance of the API class
api_instance = lib_agent.DefaultApi()
name = 'name_example' # str | Name of the Agent

try:
    api_response = api_instance.get_agent(name)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DefaultApi->get_agent: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **name** | **str**| Name of the Agent | 

### Return type

[**list[Addr]**](Addr.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Response Should contain 3 Addr Response[0] Agent Addr Response[1] Agent Is Alive endpoint Addr Response[2] Agent Documentation Addr  |  -  |
**0** | unexpected error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_agents_by_function**
> list[list[Addr]] get_agents_by_function(name)



Get the agents that match with the function name passed as params

### Example

```python
from __future__ import print_function
import time
import lib_agent
from lib_agent.rest import ApiException
from pprint import pprint

# Create an instance of the API class
api_instance = lib_agent.DefaultApi()
name = 'name_example' # str | Name of the Function

try:
    api_response = api_instance.get_agents_by_function(name)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DefaultApi->get_agents_by_function: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **name** | **str**| Name of the Function | 

### Return type

**list[list[Addr]]**

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Get the agents endpoints([3]Addr) that represent the active agents that follow the function name  |  -  |
**0** | unexpected error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_agents_names**
> list[str] get_agents_names()



Get all agents names registered in the platforms 

### Example

```python
from __future__ import print_function
import time
import lib_agent
from lib_agent.rest import ApiException
from pprint import pprint

# Create an instance of the API class
api_instance = lib_agent.DefaultApi()

try:
    api_response = api_instance.get_agents_names()
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DefaultApi->get_agents_names: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

**list[str]**

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | get all Agents |  -  |
**0** | unexpected error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_peers**
> list[Addr] get_peers()



Return all peers connected to the platform network 

### Example

```python
from __future__ import print_function
import time
import lib_agent
from lib_agent.rest import ApiException
from pprint import pprint

# Create an instance of the API class
api_instance = lib_agent.DefaultApi()

try:
    api_response = api_instance.get_peers()
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DefaultApi->get_peers: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

[**list[Addr]**](Addr.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | get Peers response |  -  |
**0** | unexpected error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_similar_agent**
> Agent get_similar_agent(name)



Get the agents that are similars to the agent passed as paramerter

### Example

```python
from __future__ import print_function
import time
import lib_agent
from lib_agent.rest import ApiException
from pprint import pprint

# Create an instance of the API class
api_instance = lib_agent.DefaultApi()
name = 'name_example' # str | Name of the Agent

try:
    api_response = api_instance.get_similar_agent(name)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DefaultApi->get_similar_agent: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **name** | **str**| Name of the Agent | 

### Return type

[**Agent**](Agent.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Get the agent that are similar |  -  |
**0** | unexpected error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **register_agent**
> register_agent(agent)



Register a new Agent in the platform

### Example

```python
from __future__ import print_function
import time
import lib_agent
from lib_agent.rest import ApiException
from pprint import pprint

# Create an instance of the API class
api_instance = lib_agent.DefaultApi()
agent = lib_agent.Agent() # Agent | Agent to register

try:
    api_instance.register_agent(agent)
except ApiException as e:
    print("Exception when calling DefaultApi->register_agent: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **agent** | [**Agent**](Agent.md)| Agent to register | 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Agent registered |  -  |
**0** | unexpected error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

