function versleutel(){
    var request = new XMLHttpRequest()
    request.open('POST', 'https://8jt1fbfdrc.execute-api.eu-central-1.amazonaws.com/dev/zin/versleutel')
    request.setRequestHeader("Content-Type", "application/json;charset=UTF-8");

    request.addEventListener("readystatechange", function () {
        if (this.readyState === 4) {
            var response = JSON.parse(this.responseText);
            console.log(this.responseText);
            document.getElementById("versleuteld").value = response.resultaat;
        }
    });

    var versleutelVraag = {
        "zin" : document.getElementById("zin").value,
        "sleutel" :  document.getElementById("sleutel").value
    }

    request.send(JSON.stringify(versleutelVraag));
}

function ontsleutel(){
    var request = new XMLHttpRequest()
    request.open('POST', 'https://8jt1fbfdrc.execute-api.eu-central-1.amazonaws.com/dev/zin/ontsleutel')
    request.setRequestHeader("Content-Type", "application/json;charset=UTF-8");

    request.addEventListener("readystatechange", function () {
        if (this.readyState === 4) {
            var response = JSON.parse(this.responseText);
            console.log(this.responseText);
            document.getElementById("zin").value = response.resultaat;
        }
    });

    var ontsleutelVraag = {
        "zin" : document.getElementById("versleuteld").value,
        "sleutel" :  document.getElementById("sleutel").value
    }

    // Send request
    request.send(JSON.stringify(ontsleutelVraag));
}