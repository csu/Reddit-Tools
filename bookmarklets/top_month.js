javascript:(function(){var e="month";var t=window.location.toString();if(t.charAt(t.length-1)!=="/"){t+="/"}if(t.indexOf("top/")!=-1){t=t.substring(0,t.indexOf("top/"))}t+="top/?sort=top&t="+e;window.location=t})()