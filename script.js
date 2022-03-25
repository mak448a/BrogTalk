function handleUrl() {
    let urlElement = document.getElementById("url");

    let downloadLink = document.getElementById("download-link");

    let url = urlElement.value;
    url += ".mp3?localembed=download";

    downloadLink.href = url;
    downloadLink.innerHTML = "<button class='btn btn-secondary'>Download Now!!!</button><br>"
    downloadLink.style.visibility = "visible"

}
