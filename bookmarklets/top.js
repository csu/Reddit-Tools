javascript:(function(){
    var time = 'year';
    var str = window.location.toString();
    if (str.charAt(str.length-1) !== '/') {
        str += '/';
    }
    if (str.indexOf("top/") != -1) {
        str = str.substring(0, str.indexOf("top/"));
    }
    str += 'top/?sort=top&t=' + time;
    window.location = str;
})();