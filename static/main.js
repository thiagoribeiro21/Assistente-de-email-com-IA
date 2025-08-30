// static/main.js
// Script principal para manipulação do formulário e exibição dos resultados
const form = document.getElementById("emailForm");
const resultsDiv = document.getElementById("results");
const spinner = document.getElementById("spinner");

form.addEventListener("submit", async (event) => {
  event.preventDefault(); // Impede o envio padrão do formulário

  // Pega os dados do formulário
  const emailText = document.getElementById("emailText").value;
  const emailFile = document.getElementById("emailFile").files[0];

  // Cria um objeto FormData para enviar texto e arquivo
  const formData = new FormData();
  if (emailFile) {
    formData.append("email_file", emailFile);
  } else if (emailText) {
    formData.append("email_text", emailText);
  } else {
    alert("Por favor, insira um texto ou selecione um arquivo.");
    return;
  }

  // Mostra o spinner e esconde resultados antigos
  spinner.style.display = "block";
  resultsDiv.style.display = "none";

  try {
    // Faz a requisição para o backend
    const response = await fetch("/processar", {
      method: "POST",
      body: formData, // Envia o FormData
    });

    const data = await response.json();

    if (response.ok) {
      // Exibe os resultados
      document.getElementById("category").textContent = data.categoria;
      document.getElementById("confidence").textContent = data.confianca;
      document.getElementById("suggestedReply").textContent =
        data.sugestao_resposta;
      resultsDiv.style.display = "block";
    } else {
      // Exibe o erro
      alert(`Erro: ${data.error}`);
    }
  } catch (error) {
    console.error("Erro na requisição:", error);
    alert("Ocorreu um erro ao se comunicar com o servidor.");
  } finally {
    // Esconde o spinner
    spinner.style.display = "none";
  }
});
