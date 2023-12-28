let postLiked = false;
let postLikeCount = 0;

function likePost() {
if (!postLiked) {
postLikeCount++;
document.getElementById("post-like-count").innerHTML = postLikeCount;
document.getElementById("post-like-btn").classList.add("liked");
document.getElementById("like-img").src = "img/serdseauto1.png"; // меняем фотографию на заполненное сердце
postLiked = true;
} else {
postLikeCount--;
document.getElementById("post-like-count").innerHTML = postLikeCount;
document.getElementById("post-like-btn").classList.remove("liked");
document.getElementById("like-img").src = "img/serdseauto.svg"; // меняем фотографию на пустое сердце
postLiked = false;
}
}