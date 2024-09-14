var audio = document.getElementById("player");
var playlist = document.querySelectorAll("#list li");
var tracks = ["HTML, CSS, JS\Music Player App\Bruno Mars - Just the Way You Are.mp3", "HTML, CSS, JS\Music Player App\Bruno Mars - Leave the Door Open.mp3", "HTML, CSS, JS\Music Player App\Bruno Mars - Locked Out Of Heaven.mp3"];
var tracksIndex = 0;


function playpause(){
    if (audio.paused){
        audio.play();
        updatePlayPauseBTN(true);
    }
    else{
        audio.pause();
        updatePlayPauseBTN(false);
    }
}

function updatePlayPauseBTN(isPlaying){
    var playPauseBTN = document.getElementById("play");
    playPauseBTN.innerText = isPlaying?'pause':'play';
}

function playNextTrack(){
    tracksIndex = (tracksIndex + 1)% tracks.length;
    changeTrack(tracks[tracksIndex], playlist[tracksIndex]);
}

function playPreviousTrack(){
    tracksIndex = (tracksIndex - 1)% tracks.length;
    changeTrack(tracks[tracksIndex], playlist[tracksIndex]);
}

function changeTrack(source, element){
    audio.src = source;
    audio.play();
    updatePlayPauseBTN(true);
    updatePlayListHighlight(element);
}

function updatePlayListHighlight(element){
    if (element){
        playlist.forEach(li => li.classList.remove("playing"));
        element.classList.add("playing");
    }
}

audio.addEventListener("ended", playNextTrack);

audio.addEventListener("timeupdate", function(){
    var progressBar = document.getElementById("progress");
    if (!isNaN(audio.duration)){
        var percentage = Math.floor((100/audio.duration)*audio.currentTime);
        progressBar.style.width = percentage + "%";
    }
});

audio.addEventListener("error", function(){
    alert("failed to load audio file");
});

playlist.forEach((item, index) => {
    item.addEventListener("click", function(){
        tracksIndex = index;
        changeTrack(tracks[tracksIndex], this);
    });
});

window.onload = function(){
    changeTrack(tracks[0], playlist[0]);
};

//Chatgpt link for error checks : https://chatgpt.com/c/66e517e4-565c-800b-b24a-d7e4cd05bc17