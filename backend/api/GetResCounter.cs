using System.Collections.Generic;
using System.Net;
using Microsoft.Azure.Functions.Worker;
using Microsoft.Azure.Functions.Worker.Http;
using Microsoft.Extensions.Logging;
using System.Text.Json.Serialization;


namespace Company.Function
{
    public static class GetResCounter
    {
        [Function("GetResCounter")]
        [CosmosDBOutput("%DatabaseName%", "%CollectionName%", ConnectionStringSetting = "CosmosDBConnectionString")]
        public static object Run([HttpTrigger(AuthorizationLevel.Function, "get", "post")] HttpRequestData req,
        [CosmosDBInput("%DatabaseName%", "%CollectionName%", ConnectionStringSetting = "CosmosDBConnectionString", Id = "1", PartitionKey = "1")] CounterJson counter,
            FunctionContext executionContext)
        {
            counter.Count++;
            return counter;
        }
    }

    public class CounterJson
    {
        [JsonPropertyName("id")]
        public string Id {get;set;}
        [JsonPropertyName("count")]
        public int Count {get;set;}
    }
}
