javascript:(function(){
    var time = 'year';
    var str = window.location.toString();
    str = str.substring(0, str.indexOf("top/"));
    str += 'top/?sort=top&t=' + time;
    window.location = str;
})();