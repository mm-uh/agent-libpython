# lib_agent.DefaultApi

All URIs are relative to *http://agentplatform.grs.uh.cu/api/v1*

Method | HTTP request | Description
------------- | ------------- | -------------
[**add_endpoints**](DefaultApi.md#add_endpoints) | **POST** /addEndpoints | 
[**edit_agent**](DefaultApi.md#edit_agent) | **POST** /editAgent | 
[**get_agent**](DefaultApi.md#get_agent) | **GET** /getAgent/{Name} | 
[**get_agents_by_function**](DefaultApi.md#get_agents_by_function) | **GET** /getAgentsForFunction/{Name} | 
[**get_agents_names**](DefaultApi.md#get_agents_names) | **GET** /getAllAgentsNames | 
[**get_functions_names**](DefaultApi.md#get_functions_names) | **GET** /getAllFunctionsNames | 
[**get_peers**](DefaultApi.md#get_peers) | **GET** /getPeers | 
[**get_similar_agent**](DefaultApi.md#get_similar_agent) | **GET** /getSimilarAgents/{Name} | 
[**recover_agent**](DefaultApi.md#recover_agent) | **POST** /recoverAgent | 
[**register_agent**](DefaultApi.md#register_agent) | **POST** /registerAgent | 


# **add_endpoints**
> add_endpoints(body)



Add endpoints to an agent in the platform

### Example

```python
from __future__ import print_function
import time
import lib_agent
from lib_agent.rest import ApiException
from pprint import pprint

# Create an instance of the API class
api_instance = lib_agent.DefaultApi()
body = lib_agent.UpdaterAgent() # UpdaterAgent | Endpoints to add

try:
    api_instance.add_endpoints(body)
except ApiException as e:
    print("Exception when calling DefaultApi->add_endpoints: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**UpdaterAgent**](UpdaterAgent.md)| Endpoints to add | 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: */*

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Endpoints added |  -  |
**0** | unexpected error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **edit_agent**
> edit_agent(body)



Edit a registered Agent in the platform

### Example

```python
from __future__ import print_function
import time
import lib_agent
from lib_agent.rest import ApiException
from pprint import pprint

# Create an instance of the API class
api_instance = lib_agent.DefaultApi()
body = lib_agent.Agent() # Agent | Agent to edit

try:
    api_instance.edit_agent(body)
except ApiException as e:
    print("Exception when calling DefaultApi->edit_agent: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**Agent**](Agent.md)| Agent to edit | 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: */*

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Agent edited |  -  |
**0** | unexpected error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

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
 - **Accept**: */*

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
 - **Accept**: */*

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
 - **Accept**: */*

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | get all Agents |  -  |
**0** | unexpected error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_functions_names**
> list[str] get_functions_names()



Get all functions names registered in the platforms 

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
    api_response = api_instance.get_functions_names()
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DefaultApi->get_functions_names: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

**list[str]**

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: */*

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | get all functions |  -  |
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
 - **Accept**: */*

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | get Peers response |  -  |
**0** | unexpected error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_similar_agent**
> list[str] get_similar_agent(name)



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

**list[str]**

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: */*

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Get the agent that are similar |  -  |
**0** | unexpected error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **recover_agent**
> Agent recover_agent(body)



Recover an agent in the platform

### Example

```python
from __future__ import print_function
import time
import lib_agent
from lib_agent.rest import ApiException
from pprint import pprint

# Create an instance of the API class
api_instance = lib_agent.DefaultApi()
body = lib_agent.RecoverAgent() # RecoverAgent | Recover agent params

try:
    api_response = api_instance.recover_agent(body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DefaultApi->recover_agent: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**RecoverAgent**](RecoverAgent.md)| Recover agent params | 

### Return type

[**Agent**](Agent.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: */*

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Agent returned |  -  |
**0** | unexpected error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **register_agent**
> register_agent(body)



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
body = lib_agent.Agent() # Agent | Agent to register

try:
    api_instance.register_agent(body)
except ApiException as e:
    print("Exception when calling DefaultApi->register_agent: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**Agent**](Agent.md)| Agent to register | 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: */*

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Agent registered |  -  |
**0** | unexpected error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

