using Microsoft.AspNetCore.Mvc;


namespace MessagesAPI.Controllers;

[ApiController]
[Route("[controller]")]
public class MessagesController : ControllerBase
{
    
    private readonly Analyzer.AnalyzerClient _serviceClient;
    public MessagesController(Analyzer.AnalyzerClient serviceClient)
    {
        _serviceClient = serviceClient;
    }

    [HttpGet("ParseMessage")]
    public ActionResult GetMessageLength(string message)
    {
        var response = _serviceClient.Analyze(new InputMessage { Payload = message});
        int messageLen = response.Result;
        return Ok(messageLen);
    }
   
}
