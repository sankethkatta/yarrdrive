var picker;
var _gaq = [['_setAccount', 'UA-23923966-1'], ['_setDomainName', 'ebaumstein.com'], ['_trackPageview']];
google.load('picker', '1');
google.setOnLoadCallback(function() {
  var view = new google.picker.View(google.picker.ViewId.DOCS);
  //var view = new google.picker.View(google.picker.ViewId.DOCS_VIDEOS);
  view.setMimeTypes('video/mp4,video/quicktime,video/mpeg,video/x-msvideo,video/x-dv,video/x-matroska,video/webm');
  picker = new google.picker.PickerBuilder()
    //.enableFeature(google.picker.Feature.NAV_HIDDEN)
    .enableFeature(google.picker.Feature.MULTISELECT_ENABLED)
    .hideTitleBar()
    //.setAuthUser('trojanwolf@gmail.com') //Optional: The user ID or email from the UserInfo API.
    .addView(view)
    //.addView(new google.picker.DocsUploadView())
    .setCallback(callback)
    .build();
});

function callback(data) {
  if (data.action == google.picker.Action.PICKED) {
    var form = document.createElement('form');
    form.setAttribute('method', 'POST');
    for (var i in data.docs) {
      var video = data.docs[i];
      console.log(video);
      form.innerHTML += '<input type="hidden" name="uid" value="'+video.id+'">';
      form.innerHTML += '<input type="hidden" name="url" value="'+video.url+'">';
      form.innerHTML += '<input type="hidden" name="raw_url" value="'+video.embedUrl+'">';
      form.innerHTML += '<input type="hidden" name="duration" value="'+video.duration+'">';
      //form.innerHTML += '<input type="hidden" name="thumbnail" value="'+video.thumbnails[2].url+'">';
      form.innerHTML += '<input type="hidden" name="name" value="'+video.name.match(/[\ \w]+/g).join('')+'">';
    }
    document.body.appendChild(form);
    form.submit();
  }
}

