function printDate()
{
    var d = new Date();
    document.write(d.toLocaleString());
}

var WastedTime = 
{
    start: new Date(),
    displayElapsed: function() 
    {
	var now = new Date();
	var elapsed = Math.round((now - WastedTime.start)/1000);
	window.defaultStatus = "you wasted " + elapsed + " seconds.";
    }
}

