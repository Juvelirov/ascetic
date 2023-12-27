function likePost() {
    var likeBtn = document.getElementById("post-like-btn"); // получаем кнопку "Нравится"
    var likeCount = parseInt(likeBtn.innerText); // получаем текущее количество лайков
    if (likeBtn.classList.contains("liked")) { // если кнопка уже была нажата
    likeCount--; // уменьшаем количество лайков на 1
    likeBtn.classList.remove("liked"); // убираем класс "liked"
    } else { // если кнопка еще не была нажата
    likeCount++; // увеличиваем количество лайков на 1
    likeBtn.classList.add("liked"); // добавляем класс "liked"
    }
    likeBtn.innerText = likeCount + 'img/Subtrect.png' + " Нравится"; // обновляем текст на кнопке
    }