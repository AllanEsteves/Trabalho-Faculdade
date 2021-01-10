# Trabalho-Faculdadefrom flask import Flask
from flask import render_template
app=Flask(__name__)

@app.route("/historia.html")
def historia():
    return render_template("historia.html")

@app.route("/copa.html")   
def copa():
    return render_template("copa.html")

@app.route("/jogadores.html")
def jogadores():
    return render_template("jogadores.html")

@app.route("/noticia.html")
def noticia():
    return render_template("noticia.html")

app.run()


#"http://127.0.0.1:5000/home" #enderco URL

#localhost:5000/home  # outro caminho q da pra por de URL

<!DOCTYPE html>
<html lang="pt-br">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <link rel="stylesheet" href="style2.css">
    <title>Partidas</title>
</head>
<body>
    <!-- Geral -->
    <div id="geral">
        <!-- Cabeçalho -->
        <div id="topo">
            <input type="checkbox" id="check">
            <label for="check"> <img src="https://assets.stickpng.com/thumbs/588a64f5d06f6719692a2d13.png"></label>
            <nav>
                <ul>
                    <li><a href="historia.html">HomePage</a></li>
                    <li><a href="jogadores.html">Times</a></li>
                    <li><a href="noticias.html">Futebol</a></li>
                </ul>
            </nav>
    </div>
    <h1>
        <h2><a>
        ■   Copa Libertadores 2020
        São Paulo x Dep. Binacional-PER
        Data: 20/10/2020
        Estádio: Morumbi - São Paulo
        Horário: 21h30
        </a></h2>
        <h2><a><br/>
        ■   Campeonato Brasileiro 2020
        Coritiba x São Paulo
        Data: 04/10/2020
        Estádio: Couto Pereira - Curitiba (PR)
        Horário: 16h00
        </a></h2>
        <h2><a> <br/>
        ■   Campeonato Brasileiro 2020
        São Paulo x Atlético-GO
        Data: 07/10/2020
        Estádio: Morumbi - São Paulo (SP)
        Horário: 20h30
        </a></h2>
        <h2><a><br/>
        ■   Campeonato Brasileiro 2020
        Palmeiras x São Paulo
        Data: 10/10/2020
        Estádio: Allianz Parque - São Paulo (SP)
        Horário: 19h00
        </a></h2>
        <h2><a><br/>
        ■   Campeonato Brasileiro 2020
        São Paulo x Grêmio
        Data: 17/10/2020
        Estádio: Morumbi - São Paulo (SP)
        Horário: 21h00
        </a></h2>
        <h2><a><br/>
        ■   Copa do Brasil 2020
        Fortaleza x São Paulo
        Data: 14/10/2020
        Estádio: Castelão - Fortaleza (CE)
        Horário: 19h15
        </a></h2>
        <h2><a><br/>
        ■   Copa do Brasil 2020
        São Paulo x Fortaleza
        Data: 25/10/2020
        Estádio: Morumbi - São Paulo (SP)
        Horário: 20h30
        </a></h2>
        <style>
            *{
                padding: 0px;
                margin: 0px;
            }
            
            body{

                height: 900px;
                background-image: url("https://i.pinimg.com/originals/73/e3/fe/73e3fe9fa7ea302c3d6ba4f430ffdf5c.jpg");
                background-size: 100%;
                background-color: rgba(16,16,16,0.5);
            }
            
            #geral{
                width: 100%;
                height: 100%;
            }
            
            #topo{
                width: 100%;
                height: 20%;
            }
            
            #lado{
                width: 10%;
                height: 60%;
      
            }
            
            #baixo{
                width: 100%;
                height: 20%;
                
            }
            
            a{
                text-decoration: none;
                color: white;
                display: block; 
                padding: 20px 5px;
                text-align: center;
            }
            a:hover{
                background-color: rgb(176,224,230);
                color: black;
            }
            
            
            ul{
                list-style: none;  
                top: 70px;
                position: absolute;
                width: 100%;
            }
            
            img{
                width: 40px;
            }
            
            input[type="checkbox"]{
                display: none;
            }
            
            input[type="checkbox"]:checked ~ nav{
                transform: translateX(350px);
            }
            
            nav{
                background-color: rgba(16,16,16,0.5);
                width: 300px;
                position: absolute;
                height: 100%;
                left: -350px;
                transition: all 1s;
            }
            
            label{
                padding: 15px;
                position: absolute;
                z-index: 1;
            }
            
            h1{
                color:grey;
                text-align: center;
            }
            h2{
                color:grey;
                text-align: center;
                margin-left: 15%;
            }
            
            
        </style>

    </h1>
</body>
</html>
<!DOCTYPE html>
<html lang="pt-br">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <link rel="stylesheet" href="style.css">
    <title>Home Page</title>
</head>
<body>
    <!-- Geral -->
    <div id="geral">
        <!-- Cabeçalho -->
        <div id="topo">
            <input type="checkbox" id="check">
            <label for="check"> <img src="https://assets.stickpng.com/thumbs/588a64f5d06f6719692a2d13.png"></label>
            <nav>
                <ul>
                    <li><a href="partidas.html">Partidas</a></li>
                    <li><a href="times.html">Times</a></li>
                    <li><a href="noticias.html">Futebol</a></li>
                    <li><a href="cadastrar.html"></a>Cadastrar</li>
                    <li><a href="novas_partid">Novas partidas</a></li>
                </ul>
            </nav>
    </div>
    <div class="articles">
        <h1>História do Futebol</h1><br/>
        <article>
        <h3>O que é o futebol?</h3><br/>
            <p><h2>O futebol (do inglês football), também conhecido por soccer nos Estados Unidos, é um desporto que coloca duas equipas,<br/>
                formadas por onze jogadores cada (dez jogadores de campo e um guarda-redes), para se confrontarem. O objectivo é fazer entrar a bola na baliza da equipa adversária,
                respeitando uma série regras.</h2><br/>
            </article>

        <article>
        <h3>O futebol no Brasil</h3><br/>
        <p>O futebol chegou ao Brasil em 1894. Charles Miller, um jovem filho de ingleses que chegou a São Paulo após realizar seus estudos na Europa, trouxe consigo bolas e regras para a prática do futebol no país.<br/>
            A prática do futebol, no Brasil, foi realizada pela primeira vez pelo São Paulo Athletic Club, formado por colonos ingleses, mas o primeiro clube formado, especialmente para a prática do futebol, foi a Associação Atlética Mackenzie College, em 1898.<br/>
            O crescimento do futebol no Brasil acabou fazendo com que o esporte mais praticado na época, o remo, viesse a ficar em segundo plano, chegando a ser quase esquecido pelos brasileiros posteriormente. Com isso, algumas equipes de remo tornaram-se clubes de futebol, como o Flamengo, Vasco da Gama e Botafogo, no Rio de Janeiro.<br/>
            A primeira equipe de futebol carioca foi o Fluminense Football Clube, fundado no ano de 1902. Também foi a primeira equipe a cobrar ingressos para uma partida de futebol no Brasil, realizada contra o Paulistano, quando, aproximadamente, 2500 pessoas acompanharam o duelo. Esse jogo também foi marcado como o primeiro que teve o comparecimento de um chefe de Estado, o então Presidente da República Rodrigues Alves.</p><br/>
        </article>

    </div>
    <style>
        *{
            padding: 0px;
            margin: 0px;
        }
        
        body{
            height: 500px;
            background-image: url("https://i.pinimg.com/originals/73/e3/fe/73e3fe9fa7ea302c3d6ba4f430ffdf5c.jpg");
            background-size: 100%;
            background-color: rgba(16,16,16,0.5);
        }
        
        #geral{
            width: 100%;
            height: 100%;
        }
        
        #topo{
            width: 100%;
            height: 20%;
        }
        
        #lado{
            width: 10%;
            height: 60%;
            background-color: lightskyblue;
        }
        
        #baixo{
            width: 100%;
            height: 20%;
            background-color: lime;
        }
        
        a{
            text-decoration: none; 
            color: white;
            display: block; 
            padding: 20px 5px;
            text-align: center;
        }
        a:hover{
            background-color: rgb(176,224,230);
            color: black;
        }
        
        
        ul{
            list-style: none; 
            top: 70px;
            position: absolute;
            width: 100%;
        }
        
        img{
            width: 40px;
        }
        
        input[type="checkbox"]{
            display: none;
        }
        
        input[type="checkbox"]:checked ~ nav{
            transform: translateX(350px);
        }
        
        nav{
            background-color: rgba(16,16,16,0.5);
            width: 300px;
            position: absolute;
            height: 100%;
            left: -350px;
            transition: all 1s;
        }
        
        label{
            padding: 15px;
            position: absolute;
            z-index: 1;
        }
        
        h1{
            color:grey;
            text-align: center;
        }
        h2{
            color:grey;
            text-align: center;
            margin-left: 15%;
        }
        div.articles h1{
            width: auto;
            color: white;
            padding: 20px;
        }

        div.articles {
            width:70%;
            margin: 0 auto;
            font-size: 15px; 
            padding: 20px;
            color: white;
            box-sizing: border-box;
            font-family: Arial, Helvetica, sans-serif;
        }

        div.articles article {
            background-color: rgba(0, 0, 0, 0.55);
            padding: 10px;
            box-sizing: border-box;
            margin-bottom: 20px;
        }
        
    </style>
    </h1>
</body>
</html>
<!DOCTYPE html>
<html lang="pt-br">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <link rel="stylesheet" href="style2.css">
    <title>Times</title>
</head>
<body>
    <!-- Geral -->
    <div id="geral">
        <!-- Cabeçalho -->
        <div id="topo">
            <input type="checkbox" id="check">
            <label for="check"> <img src="https://assets.stickpng.com/thumbs/588a64f5d06f6719692a2d13.png"></label>
            <nav>
                <ul>
                    <li><a href="historia.html">HomePage</a></li>
                    <li><a href="copa.html">Partidas</a></li>
                    <li><a href="noticias.html">Futebol</a></li>
                </ul>
            </nav>
    </div>
    <table border=4>
        <tr>
            <h3>ㅤㅤㅤㅤㅤㅤㅤㅤㅤㅤㅤCoritibaㅤㅤㅤㅤㅤㅤㅤㅤㅤㅤㅤㅤㅤㅤㅤㅤㅤㅤㅤSão Paulo</h3>
        </tr>
        <tr>
    
            <td>
                <h4>ㅤJogadores</h4>
            </td>
            <td>
                <h4>ㅤPeso</h4>
            </td>
            <td>
                <h4>ㅤVelocidade</h4>
            </td>
            <td>
                <h4>ㅤCamiseta</h4>
            </td>
            <td>
                <h4>ㅤIdadeㅤㅤㅤㅤㅤJogadores ㅤPesoㅤVelocidadeㅤCamisetaㅤIdade</h4>
            </td>
        </tr>
    
        <tr>
            <td>ㅤㅤJoão</td>
            <td>ﾠﾠ72kg</td>
            <td>ㅤㅤ30km/h</td>
            <td>ㅤㅤㅤ5</td>
            <td>ㅤﾠ22ㅤㅤㅤㅤㅤㅤㅤCarlosㅤㅤ62kgㅤㅤ30km/hㅤㅤㅤ7ㅤㅤㅤ20</td>
    
        </tr>
        <tr>
            <td>ㅤㅤLeo</td>
            <td>ﾠﾠ76kg</td>
            <td>ㅤㅤ31,02km/h</td>
            <td>ㅤㅤㅤ29</td>
            <td>ㅤﾠ31ㅤㅤㅤㅤㅤㅤㅤWesleyㅤﾠ82kgㅤㅤ28km/hㅤㅤㅤ22ㅤㅤㅤ19</td>
    
        </tr>
        <tr>
            <td>ㅤㅤCleber</td>
            <td>ﾠﾠ80kg</td>
            <td>ㅤㅤ29,80km/h</td>
            <td>ㅤㅤㅤ7</td>
            <td>ﾠㅤ19ㅤㅤㅤㅤㅤㅤㅤGabrielㅤﾠ83kgㅤㅤ29,70km/hㅤㅤ35ㅤㅤㅤ23</td>
    
        </tr>
        <tr>
            <td>ㅤㅤMarcos</td>
            <td>ﾠﾠ68kg</td>
            <td>ㅤㅤ33km/h</td>
            <td>ㅤㅤㅤ22</td>
            <td>ㅤﾠ25ㅤㅤㅤㅤㅤㅤㅤThiagoㅤﾠ68kgㅤㅤ30,45km/hㅤㅤ47ㅤㅤㅤ33</td>
    
        </tr>
        <tr>
            <td>ㅤㅤMiguel</td>
            <td>ﾠﾠ74kg</td>
            <td>ㅤㅤ31,80km/h</td>
            <td>ㅤㅤㅤ16</td>
            <td>ㅤﾠ27ㅤㅤㅤㅤㅤㅤㅤViniciusㅤ72kgㅤㅤ29km/hㅤㅤㅤ41ㅤㅤㅤ18</td>
    
        </tr>
        <tr>
            <td>ㅤㅤAntonio</td>
            <td>ﾠﾠ69kg</td>
            <td>ㅤㅤ32,20km/h</td>
            <td>ㅤㅤㅤ31</td>
            <td>ㅤﾠ30ㅤㅤㅤㅤㅤㅤㅤAlanㅤㅤﾠ77kgㅤㅤ33km/hㅤㅤㅤ56ㅤㅤㅤ31</td>
    
        </tr>
        <tr>
            <td>ㅤㅤCarlos</td>
            <td>ﾠﾠ72kg</td>
            <td>ㅤㅤ30km/h</td>
            <td>ㅤㅤㅤ5</td>
            <td>ㅤﾠ22ㅤㅤㅤㅤㅤㅤㅤPedroㅤㅤ69kgㅤㅤ31km/hㅤㅤㅤ29ㅤㅤㅤ28</td>
    
        </tr>
    </table>
    <table border=4>
        <tr>
            <h3>ㅤㅤㅤㅤㅤㅤㅤㅤㅤㅤㅤSão PauloㅤㅤㅤㅤㅤㅤㅤㅤㅤㅤㅤㅤㅤㅤㅤㅤㅤㅤAtlético-GO</h3>
        </tr>
        <tr>
    
            <td>
                <h4>ㅤJogadores</h4>
            </td>
            <td>
                <h4>ㅤPeso</h4>
            </td>
            <td>
                <h4>ㅤVelocidade</h4>
            </td>
            <td>
                <h4>ㅤCamiseta</h4>
            </td>
            <td>
                <h4>ㅤIdadeㅤㅤㅤㅤㅤJogadores ㅤPesoㅤVelocidadeㅤCamisetaㅤIdade</h4>
            </td>
        </tr>
    
        <tr>
            <td>ㅤㅤCarlos</td>
            <td>ﾠﾠ70kg</td>
            <td>ㅤㅤ30km/h</td>
            <td>ㅤㅤㅤ2</td>
            <td>ㅤﾠ38ㅤㅤㅤㅤㅤㅤㅤMatheusㅤﾠ85kgㅤㅤ26km/hㅤㅤㅤ31ㅤㅤㅤ36</td>
    
        </tr>
        <tr>
            <td>ㅤㅤLeandro</td>
            <td>ﾠﾠ78kg</td>
            <td>ㅤㅤ33,21km/h</td>
            <td>ㅤㅤㅤ8</td>
            <td>ㅤﾠ28ㅤㅤㅤㅤㅤㅤㅤLuanㅤㅤﾠﾠ74kgㅤㅤ27km/hㅤㅤㅤ18ㅤㅤㅤ21</td>
    
        </tr>
        <tr>
            <td>ㅤㅤGustavo</td>
            <td>ﾠﾠ76kg</td>
            <td>ㅤㅤ30,60km/h</td>
            <td>ㅤㅤㅤ33</td>
            <td>ﾠㅤ23ㅤㅤㅤㅤㅤㅤㅤDouglasㅤﾠ71kgㅤㅤ31km/hㅤㅤㅤ21ㅤㅤㅤ23</td>
    
        </tr>
        <tr>
            <td>ㅤㅤVinicius</td>
            <td>ﾠﾠ72kg</td>
            <td>ㅤㅤ28km/h</td>
            <td>ㅤㅤㅤ26</td>
            <td>ㅤﾠ31ㅤㅤㅤㅤㅤㅤㅤLucasㅤㅤﾠ77kgㅤㅤ33km/hㅤㅤㅤ25ㅤㅤㅤ25</td>
    
        </tr>
        <tr>
            <td>ㅤㅤAlison</td>
            <td>ﾠﾠ63kg</td>
            <td>ㅤㅤ34km/h</td>
            <td>ㅤㅤㅤ35</td>
            <td>ㅤﾠ27ㅤㅤㅤㅤㅤㅤㅤHenriqueﾠﾠ59kgㅤㅤ34km/hㅤㅤㅤ33ㅤㅤㅤ27</td>
    
        </tr>
        <tr>
            <td>ㅤㅤMessias</td>
            <td>ﾠﾠ67kg</td>
            <td>ㅤㅤ34,04km/h</td>
            <td>ㅤㅤㅤ18</td>
            <td>ㅤﾠ34ㅤㅤㅤㅤㅤㅤㅤOsvaldoㅤﾠ68kgㅤㅤ28km/hㅤㅤㅤ37ㅤㅤㅤ30</td>
    
        </tr>
        <tr>
            <td>ㅤㅤNatan</td>
            <td>ﾠﾠ72kg</td>
            <td>ㅤㅤ28km/h</td>
            <td>ㅤㅤㅤ26</td>
            <td>ㅤﾠ31ㅤㅤㅤㅤㅤㅤㅤWagnerㅤﾠ67kgㅤㅤ29km/hㅤㅤㅤ17ㅤㅤㅤ31</td>
    </table>
    <table border=4>
        <tr>
            <h3>ㅤㅤㅤㅤㅤㅤㅤㅤㅤㅤㅤPlameirasㅤㅤㅤㅤㅤㅤㅤㅤㅤㅤㅤㅤㅤㅤㅤㅤㅤㅤSão Paulo</h3>
        </tr>
        <tr>
    
            <td>
                <h4>ㅤJogadores</h4>
            </td>
            <td>
                <h4>ㅤPeso</h4>
            </td>
            <td>
                <h4>ㅤVelocidade</h4>
            </td>
            <td>
                <h4>ㅤCamiseta</h4>
            </td>
            <td>
                <h4>ㅤIdadeㅤㅤㅤㅤㅤJogadores ㅤPesoㅤVelocidadeㅤCamisetaㅤIdade</h4>
            </td>
        </tr>
    
        <tr>
            <td>ㅤㅤCarlos</td>
            <td>ﾠﾠ70kg</td>
            <td>ㅤㅤ30km/h</td>
            <td>ㅤㅤㅤ2</td>
            <td>ㅤﾠ38ㅤㅤㅤㅤㅤㅤㅤMatheusㅤ74kgㅤㅤ27km/hㅤㅤㅤ26ㅤㅤㅤ22</td>
    
        </tr>
        <tr>
            <td>ㅤㅤLeandro</td>
            <td>ﾠﾠ78kg</td>
            <td>ㅤㅤ33,21km/h</td>
            <td>ㅤㅤㅤ8</td>
            <td>ㅤﾠ28ㅤㅤㅤㅤㅤㅤㅤLuanﾠﾠㅤﾠ73kgㅤㅤ26,80km/hㅤㅤ5ㅤㅤㅤ31</td>
    
        </tr>
        <tr>
            <td>ㅤㅤGustavo</td>
            <td>ﾠﾠ76kg</td>
            <td>ㅤㅤ30,60km/h</td>
            <td>ㅤㅤㅤ33</td>
            <td>ﾠㅤ23ㅤㅤㅤㅤㅤㅤㅤDouglasﾠﾠ66kgㅤㅤ31km/hㅤㅤㅤ37ㅤㅤㅤ27</td>
    
        </tr>
        <tr>
            <td>ㅤㅤVinicius</td>
            <td>ﾠﾠ72kg</td>
            <td>ㅤㅤ28km/h</td>
            <td>ㅤㅤㅤ26</td>
            <td>ㅤﾠ31ㅤㅤㅤㅤㅤㅤㅤLucasㅤㅤ61kgㅤㅤ30km/hㅤㅤㅤ48ㅤㅤㅤ19</td>
    
        </tr>
        <tr>
            <td>ㅤㅤAlison</td>
            <td>ﾠﾠ63kg</td>
            <td>ㅤㅤ34km/h</td>
            <td>ㅤㅤㅤ35</td>
            <td>ㅤﾠ27ㅤㅤㅤㅤㅤㅤㅤHenriqueﾠ81kgㅤㅤ33km/hㅤㅤㅤ33ㅤㅤㅤ23</td>
    
        </tr>
        <tr>
            <td>ㅤㅤMessias</td>
            <td>ﾠﾠ67kg</td>
            <td>ㅤㅤ34,04km/h</td>
            <td>ㅤㅤㅤ18</td>
            <td>ㅤﾠ34ㅤㅤㅤㅤㅤㅤㅤOsvaldoﾠﾠ72kgㅤㅤ31km/hㅤㅤﾠﾠ24ㅤㅤㅤ34</td>
    
        </tr>
        <tr>
            <td>ㅤㅤNatan</td>
            <td>ﾠﾠ72kg</td>
            <td>ㅤㅤ28km/h</td>
            <td>ㅤㅤㅤ26</td>
            <td>ㅤﾠ31ㅤㅤㅤㅤㅤㅤㅤWagnerㅤﾠ65kgㅤㅤ29km/hㅤㅤﾠﾠ44ㅤㅤㅤ30</td>
    </table>
    <style>
        *{
            padding: 0px;
            margin: 0px;
        }
        
        body{
            height: 900px;
            background-image: url("https://i.pinimg.com/originals/73/e3/fe/73e3fe9fa7ea302c3d6ba4f430ffdf5c.jpg");
            background-size: 100%;
            background-color: rgba(16,16,16,0.5);
        }
        
        #geral{
            width: 100%;
            height: 100%;
        }
        
        #topo{
            width: 100%;
            height: 20%;
        }
        
        #lado{
            width: 10%;
            height: 60%;
    
        }
        
        #baixo{
            width: 100%;
            height: 20%;
          
        }
        
        a{
            text-decoration: none;
            color: white;
            display: block; 
            padding: 20px 5px;
            text-align: center;
        }
        a:hover{
            background-color: rgb(176,224,230);
            color: black;
        }
        
        
        ul{
            list-style: none; 
            top: 70px;
            position: absolute;
            width: 100%;
        }
        
        img{
            width: 40px;
        }
        
        input[type="checkbox"]{
            display: none;
        }
        
        input[type="checkbox"]:checked ~ nav{
            transform: translateX(350px);
        }
        
        nav{
            background-color: rgba(16,16,16,0.5);
            width: 300px;
            position: absolute;
            height: 100%;
            left: -350px;
            transition: all 1s;
        }
        
        label{
            padding: 15px;
            position: absolute;
            z-index: 1;
        }
        
        h1{
            color:grey;
            text-align: center;
        }
        h2{
            color:grey;
            text-align: center;
            margin-left: 15%;
        }
        table{
            margin-left:30%;
            color:white;
        }
        h3{
            margin-left:30%;
            color:white;
        }
    
    </style>
    

</body>
</html>
<!DOCTYPE html>
<html lang="pt-br">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <link rel="stylesheet" href="style2.css">
</head>
<body>
    <!-- Geral -->
    <div id="geral">
        <!-- Cabeçalho -->
        <div id="topo">
            <input type="checkbox" id="check">
            <label for="check"> <img src="https://assets.stickpng.com/thumbs/588a64f5d06f6719692a2d13.png"></label>
            <nav>
                <ul>
                    <li><a href="copa.html">HomePage</a></li>
                    <li><a href="historia.html">Partidas</a></li>
                    <li><a href="jogadores.html">Times</a></li>
                </ul>
            </nav>
    </div>
    <div class="articles">
        <h1>Noticias</h1>

        <article>
            <h3>Vasco bate o Atlético-MG e vence a primeira na Série A2 do Brasileirão Feminino</h3><br/>
            <p>O Vasco venceu o Atlético-MG por 1 a 0 pela segunda rodada da Série A2 do Brasileirão Feminino, no Estádio Nivaldo Pereira, em Nova Iguaçu, no Rio de Janeiro. Com o resultado, o Vasco chegou aos 4 pontos e subiu para a vice-liderança do Grupo E. Já o Galo conheceu a sua primeira derrota e estacionou na tabela, com apenas um ponto, na quinta colocação.<br/>
                O único gol do jogo foi marcado pela atacante Isa Rangel, aos 34 minutos do segundo tempo. A camisa 11 vascaína bateu colocado de fora da área com a perna esquerda e encobriu a goleira Amanda. Com o placar aberto, o Atlético ainda tentou buscar o empate, mas não conseguiu encontrar os espaços e transformar a posse de bola em chances claras de gol</p>
               <br/><h6>Fonte: Globo Esporte</h6><br/>
        </article>

        <article>
            <h3>Fluminense aproveita chances, bate o Sport e se aproxima da liderança do Brasileirão sub-20</h3><br/>
            <h3>O jogo</h3><br/>
            <p>Fluminense e Sport fizeram um jogo aberto, com grandes oportunidades para os dois lados. No primeiro tempo, os cariocas abriram o placar logo aos 15 minutos, com John Kennedy, de cabeça. Após o gol, o Leão não se abalou e construiu grandes oportunidades para empatar, com Luís Otávio e Ferrugem. Logo no início da segunda etapa, o Flu chegou ao segundo gol, com Cipriano, após rebote em cruzamento. O Sport novamente se lançou ao ataque e foi melhor durante boa parte do jogo. A equipe pernambucana ainda desperdiçou um pênalti, com Igor, aos 22 minutos. No fim, a vitória ficou com o Tricolor.</p><br/>
            <h6>Fonte: Globo Esporte</h6>
        </article>
    </div>
     

    <style>
        *{
            padding: 0px;
            margin: 0px;
        }
        
        body{
            background-image: url("https://i.pinimg.com/originals/73/e3/fe/73e3fe9fa7ea302c3d6ba4f430ffdf5c.jpg");
            background-size: 100%;
            background-color: rgba(16,16,16,0.5);
            background-repeat: no-repeat;
        }
        
        #geral{
            width: 100%;
            height: 100%;
        }
        
        #topo{
            width: 100%;
            height: 20%;
        }
        
        #lado{
            width: 10%;
            height: 60%;
            background-color: lightskyblue;
        }
        
        #baixo{
            width: 100%;
            height: 20%;
            background-color: lime;
        }
        
        a{
            text-decoration: none; 
            color: white;
            display: block; 
            padding: 20px 5px;
            text-align: center;
        }
        a:hover{
            background-color: rgb(176,224,230);
            color: black;
        }
        
        
        ul{
            list-style: none;  
            top: 70px;
            position: absolute;
            width: 100%;
        }
        
        img{
            width: 40px;
        }
        
        input[type="checkbox"]{
            display: none;
        }
        
        input[type="checkbox"]:checked ~ nav{
            transform: translateX(350px);
        }
        
        nav{
            background-color: rgba(16,16,16,0.5);
            width: 300px;
            position: absolute;
            height: 100%;
            left: -350px;
            transition: all 1s;
        }
        
        label{
            padding: 15px;
            position: absolute;
            z-index: 1;
        }
        
        h1{
            color:grey;
            text-align: center;
        }
        h2{
            color:grey;
            text-align: center;
            margin-left: 15%;
        }
        div.articles h1{
            width: auto;
            color: white;
            padding: 40px;
        }

        div.articles {
            width:70%;
            margin: 0 auto;
            font-size: 15px; 
            padding: 20px;
            color: white;
            box-sizing: border-box;
            font-family: Arial, Helvetica, sans-serif;
        }

        div.articles article {
            background-color: rgba(0, 0, 0, 0.55);
            padding: 10px;
            box-sizing: border-box;
            margin-bottom: 20px;
        }
            

    </style>

</body>
</html>
