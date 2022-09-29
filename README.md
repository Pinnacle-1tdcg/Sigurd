# Pinnacle

Projeto voltado a parar ransomwares e proteger arquivos 

O grupo Pinnacle, que conta com  a motivação de tornar o dia a dia de pequnas empresas e usuarios comuns mais seguras, pensando em proteger
seus arquivos, ativos, e proteger a maquina de sofrer um dano permanente em seu SISTEMA apos sofrer um ataque de ransomware.

Ferramentas:



Backup

Como um backup, ele procura arquivos em tres diretorios, "home" do usuario que executou, "/root"  que seria o home do super usuario e "/tmp" onde estao arquivos temporarios, apos pegar todos que estejam nesses diretorios (e com a extensão na lista) ele ira fazer uma copia para nossa pasta de backup que foi colocada no "/bin/"b@ck&ppinn@cl#"" por uma questao de segurança, o objetivo da maioria dos grupos que usam ransomwares é conseguir pagamente mediante extorsão das vitimas, essa pasta contem muitos arquivos do sistema que ao serem danificados a maquina pode sofrer graves problemas ou ate mesmo ficar inutilizavel, pensando nisso por ser um lugar menos visado, porem nao sendo impossivel, escolhemos salvar nesse local.


Como usar? 

Ir no diretorio que ele se encontra salvo, executar o comando "sudo python3 backup_versao_1.0.py" e ira abrir uma pequena interface, clique no botao indicado e pronto, so aguardar um momento e o backup sera realizado com sucesso.


![image](https://user-images.githubusercontent.com/114665200/193116500-7f229545-a81c-481a-a3ee-b4352c6360e4.png)

![image](https://user-images.githubusercontent.com/114665200/193116668-0f0866b4-bd47-4e63-bad1-832583a6d6a5.png)

![image](https://user-images.githubusercontent.com/114665200/193116749-5a63d99d-3874-4941-806c-1d327dd4d8cb.png)


