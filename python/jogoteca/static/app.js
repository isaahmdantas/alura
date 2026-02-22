$("form input[type=file]").on("change", function (event) {
    let arquivos = event.target.files;
    console.log(arquivos);

    if (arquivos.length === 0) {
        console.log("Nenhum arquivo selecionado");
    } else {
        if (arquivos[0].type.startsWith("image/")) {
            console.log("Arquivo selecionado é uma imagem");
            $("img").remove();
            let imagem = $("<img class='img-fluid'>");
            imagem.attr("src", window.URL.createObjectURL(arquivos[0]));
            $("figure").prepend(imagem);
        } else {
            alert("Arquivo selecionado não é uma imagem");
        }
    }


})