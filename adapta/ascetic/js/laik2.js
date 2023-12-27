let likeCoun = 0;
function likePost() {
    var likeBtn = document.getElementById("post-like-btn"); // получаем кнопку "Нравится"
    var likeCount = parseInt(likeBtn.dataset.likes); // получаем текущее количество лайков из атрибута data-likes
    var likeImg = likeBtn.querySelector(".like-img"); // получаем картинку лайка
    if (likeBtn.classList.contains("liked")) { // если кнопка уже была нажата
    likeCount=""; // уменьшаем количество лайков на 1
    likeBtn.classList.remove("liked"); // убираем класс "liked"
    likeImg.src = "img/serdseauto.svg"; // меняем картинку на серую
    likeImg.width = 30;
    likeImg.height = 30;
    } else { // если кнопка еще не была нажата
    likeCount = 1; // увеличиваем количество лайков на 1
    likeBtn.classList.add("liked"); // добавляем класс "liked"
    likeImg.src = "img/serdseauto1.png"; // меняем картинку на красную
    }
    likeBtn.dataset.likes = likeCount; // обновляем атрибут data-likes
    likeBtn.querySelector(".like-text").innerText = likeCount + " Нравится"; // обновляем текст на кнопке
    }