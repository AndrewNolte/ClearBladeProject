//This was file goes in the "Code" section of the clearblade dashboard

//also a Collection called cpu has to be made

function StoreMessageService(req, resp) {
  ClearBlade.init({
    request: req
  });

  var msg = ClearBlade.Messaging();
  var unixTimeNano = new Date().getTime();
  var unixTimeMilli = unixTimeNano / 1000;

  msg.getMessageHistoryWithTimeFrame("cpuTopic", 1, unixTimeMilli, null, null, function (err, body) {
    if (err) {
      resp.error("message history error : " + JSON.stringify(body));
    } else {
      var col = ClearBlade.Collection({
        collectionName: "cpu"
      });
      var pct = parseFloat(body[0].message);
      col.create({
        percent: pct
      }, function (err, data) {
        if (err) {
          resp.error("creation error : " + JSON.stringify(data));
        } else {
          resp.success(data);
        }
      });
    }
  });

  resp.success("Success");
}