//"use javascript to display the hour in current time zone"
var dateDisplay = function(me)
{
    var form = me;
    var link = document.getElementById('link').innerHTML;
    var linkstring = link.toString();
    var eve = false;
    if(linkstring.includes("p"))
    {
        linkstring = linkstring.replace(" p.m.", "");
        eve = true;
    }
    if(linkstring.includes("a"))
        linkstring = linkstring.replace(" a.m.", "");
    var dateNum = Date.parse(linkstring);
    var date = new Date(dateNum);
    var month = date.getMonth();
    var year = date.getFullYear();
    var day = date.getDate();
    var hour = date.getHours();
    if(eve)
        hour=hour+12;
    var minute = date.getMinutes();
    var d = new Date(year, month, day, hour - 6, minute, 0);
    document.getElementById("link").innerHTML = d;
}