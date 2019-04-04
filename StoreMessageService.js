//This was file goes in the "Code" section of the clearblade dashboard

//also a Collection called cpu has to be made

function StoreMessageService(req, resp) {
    ClearBlade.init({
        request: req
    });

    var msg = ClearBlade.Messaging();
    var unixTimeNano = new Date().getTime();
    var unixTimeMilli = unixTimeNano / 1000;

    var colec = ClearBlade.Collection({
        collectionName: "cpu"
    });
    var blob = JSON.parse(req.params.body);

    colec.create({
        percent: (Math.round(blob.pct * 10) / 10),
        timestamp: blob.timestamp
    }, function (err, data) {
        if (err) {
            resp.error("creation error : " + JSON.stringify(data));
        } else {
            resp.success(data);
        }
    });
    resp.success("Success");
}