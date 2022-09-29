Pinnacle

email para contato: pinnacle.1tdcg@proton.me

time: 

- Gustavo Gonçalves Diniz
- Leandro Sung Ha
- Leonardo de Oliveira Leitão
- Vinicius Angelo Poci


---------------------------------------------------------------------------------------------------------------------------------------------------------------

Projeto voltado a parar ransomwares e proteger arquivos 

O grupo Pinnacle, que conta com  a motivação de tornar o dia a dia de pequnas empresas e usuarios comuns mais seguras, pensando em proteger
seus arquivos, ativos, e proteger a maquina de sofrer um dano permanente em seu SISTEMA apos sofrer um ataque de ransomware.

---------------------------------------------------------------------------------------------------------------------------------------------------------------

Ferramentas:



Backup

Como um backup, ele procura arquivos em tres diretorios, "home" do usuario que executou, "/root"  que seria o home do super usuario e "/tmp" onde estao arquivos temporarios, apos pegar todos que estejam nesses diretorios (e com a extensão na lista) ele ira fazer uma copia para nossa pasta de backup que foi colocada no "/bin/"b@ck&ppinn@cl#"" por uma questao de segurança, o objetivo da maioria dos grupos que usam ransomwares é conseguir pagamente mediante extorsão das vitimas, essa pasta contem muitos arquivos do sistema que ao serem danificados a maquina pode sofrer graves problemas ou ate mesmo ficar inutilizavel, pensando nisso por ser um lugar menos visado, porem nao sendo impossivel, escolhemos salvar nesse local.


Como usar? 

Ir no diretorio que ele se encontra salvo, executar o comando "sudo python3 backup_versao_1.0.py" e ira abrir uma pequena interface, clique no botao indicado e pronto, so aguardar um momento e o backup sera realizado com sucesso.


![image](https://user-images.githubusercontent.com/114665200/193116500-7f229545-a81c-481a-a3ee-b4352c6360e4.png)

![image](https://user-images.githubusercontent.com/114665200/193116668-0f0866b4-bd47-4e63-bad1-832583a6d6a5.png)

![image](https://user-images.githubusercontent.com/114665200/193116749-5a63d99d-3874-4941-806c-1d327dd4d8cb.png)


![image](https://user-images.githubusercontent.com/114665200/193119867-5d244c87-8218-415f-908e-47cf31603cc9.png)


-----------------------------------------------------------------------------------------------------------------------------------------------------------------------

Detector

A parte de deteccao funciona de algumas formas, tem varios vetores ao mesmo tempo trabalhando para que encontre qualquer coisa que possa ser considerada uma ameaça, seja por uso de CPU, qualquer tipo de alteracao nos arquivos armadilhas, inodes ou download de arquivos com uma hash conhecida tambem a ferramenta teria capacidade de deletar esse arquivo e executar uma acao de parada de processos.

Para que isso aconteca, como no backup, a ferramenta precisa ser executa com privilegios de "root", que significa maior possivel em uma maquina linux, pois precisamos fazer algumas operacoes que somente um SUPER USUARIO poderia fazer.

A ferramenta passou por uma serie de testes com ransomwares que estao sendo disponibilizados hoje em dia e obteve sucesso na maioria dos testes, conseguindo parar eles e proteger os arquivos de backup e ate mesmo a maquina de ser danificada parando o avanco do ataque.

