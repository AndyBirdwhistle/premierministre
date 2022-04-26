import tweepy
import config
import json
import random
import regex
import datetime

personalites = """Commandant Cousteau
Abbé Pierre
Omar Sy
Haroun Tazieff
Dany Boon
Michel Cymes
Zinédine Zidane
Florence Foresti
Jean-Jacques Goldman
Sœur Emmanuelle
Gad Elmaleh
Jean Reno
Jean-Paul Belmondo
Mimie Mathy
Renaud
Yves Montand
Charles Aznavour
Jean Dujardin
Philippe Noiret
Francis Cabrel
Sophie Marceau
Michel Sardou
Henri Salvador
Florent Pagny
Michel Serrault
Robert Hossein
Anne Sinclair
Nagui
Nicolas Hulot
Yannick Noah
David Douillet
Gérard Depardieu
Jamel Debbouze
Michel Drucker
Teddy Riner
Patricia Kaas
Léon Schwartzenberg
François Mitterrand
Raymond Devos
Simone Veil
Catherine Deneuve
Florence Arthaud
Bruno Masure
Aimé Jacquet
Johnny Hallyday
Gérard Jugnot
Fabrice Luchini
Jean-Pierre Pernaut
Patrick Poivre D'Arvor
Alain Prost
Jacques-Yves Cousteau
Bernard Pivot
François Mitterrand
Jean-Paul Belmondo
Michel Drucker
Yves Montand
Robert Hossein
Michel Platini
Anne Sinclair
Bernard Tapie
Raymond Barre
Alain Delon
Jacques Chirac
Patrick Poivre d'Arvor
Catherine Deneuve
Simone Veil
Jacques Martin
Alain Prost
Michel Polac
Jean-Jacques Goldman
Daniel Auteuil
Gérard Depardieu
Mireille Mathieu
Jack Lang
Éric Tabarly
Patrick Sabatier
Jeannie Longo
François Léotard
Jean-Marie Lustiger
Michel Rocard
Valéry Giscard d'Estaing
Harlem Désir
Michèle Barzach
Isabelle Adjani
Yves Mourousi
Johnny Hallyday
Maurice Béjart
Jeanne Mas
Laurent Fignon
Stéphane Collaro
Yannick Noah
Eddy Mitchell
Jean-Marie Le Pen
Marguerite Duras
Françoise Sagan
Sophie Marceau
Georges Marchais
Francis Bouygues
Pierre Juquin
Alain Minc
Sophie Marceau
Marion Cotillard
Florence Foresti
Louane
Alexandra Lamy
Josiane Balasko
Mimie Mathy
Mylène Farmer
Valérie Lemercier
Karine Le Marchand
Anne Roumanoff
Françoise Hardy
Line Renaud
Évelyne Dhéliat
Vanessa Paradis
Michèle Laroque
Muriel Robin
Nolwenn Leroy
Zazie
Ingrid Chauvin
Faustine Bollaert
Charlotte Gainsbourg
Catherine Deneuve
Jenifer
Clara Luciani
Jean-Jacques Goldman
Thomas Pesquet
Omar Sy
Soprano
Francis Cabrel
Florent Pagny
Dany Boon
Teddy Riner
Philippe Etchebest
Jean-Pierre Pernaut
Renaud
Cyril Lignac
Vianney
Jean Reno
Jean-Luc Reichmann
Michel Sardou
Zinédine Zidane
Jean Dujardin
Kylian Mbappe
Kad Merad
Stéphane Plaza
Stéphane Bern
Christian Clavier
Julien Doré
Antoine Griezmann
Nicolas Sarkozy
Christine Lagarde
Valérie Pécresse
Xavier Bertrand
Edouard Philippe
Laurent Wauquiez
Michel Barnier
Jean-Yves Le Drian
Rachida Dati
Eric Ciotti
Roselyne Bachelot
Christian Jacob
Marine Le Pen
Marion Maréchal
Bruno Le Maire
Eric Zemmour
Nicolas Dupont-Aignan
Olivier Véran
Gabriel Attal
Jean-Michel Blanquer
Gérald Darmanin
Fabien Roussel
Eric Dupond-Moretti
Florence Parly
Marlène Schiappa
François Bayrou
Manuel Valls
Jean-Luc Mélenchon
Yannick Jadot
François Hollande
Philippe Poutou
Anne Hidalgo
Christiane Taubira"""

l = personalites.split("\n")
random.shuffle(l)


i = 0

bl = 1
while(1):
    now = datetime.datetime.now()
    
    if now.minute == 00 and bl == 1:
        print("i")
        client = tweepy.Client(
            bearer_token = "AAAAAAAAAAAAAAAAAAAAADEpbAEAAAAA27kgZvJU%2Bvk8EkR%2FonwFpWkuWRE%3Da90cHMUTLgjcJwnZLjIJDvAUyVOW0Sw7OrSCVmQJy8zJgOMHvQ",
            consumer_key="T5usu7vZy0LN4BuYWG9bxRqVg",
            consumer_secret="g4mBrHCjd0BM8bIMfJxmHlFeoCYtFnEPrhldF28yvfgTs3NheX",
            access_token="1426625347861233665-MRT8kmDxwVdBuNE2KVoUVTUMQSEXys",
            access_token_secret="qElHjqx136MzaktV4vbwl0hLjyRzNalDPPHst66TcePoC"
        )
        i += 1

        response = client.create_tweet(text='Emmanuel Macron nommera ' + l[i] + ' premier ministre.')
        bl = 0
    elif now.minute != 00:
        bl = 1



