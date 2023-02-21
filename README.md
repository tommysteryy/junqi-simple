# Junqi CLI *"Jun"*
A simple command-line "referee", *Jun*, for the traditional Chinese game 军旗 (junqi)

## Motivation
For whatever reason, the more popular games in my asian culture are two-player-ed; while popular games in western culture seem to be much more multiplayer-ed. Many of my games, I can just play with my girlfriend 1-on-1, but one of her favourites, 军旗 REQUIRES a third-party "referee" to progress the game. This is for you, love!

## What is 军旗？
军旗, pronounced "jew-n ch-ee", is a traditional, 2-player, highly-tactical board game that challenges both players to play a game of war **without ever knowing each other's pieces**. 

![Picture of the junqi board](https://images-na.ssl-images-amazon.com/images/I/51j1UanSMXL.jpg "Typical setup for Junqi")

Players start with 25 "cards" each of various "sizes" (you can see the relative sizes of each card below), and you usually play the game as shown in the picture above. You can enter a "duel" when you move one of your pieces into the space of one of your opponents', and the larger "size" piece will stay. Here is where a **third-party** must compare the sizes of the cards, and discard the smaller piece. This way, both players do not have complete information for *the entire game*.

### The "Cards"

| Card (Chinese) | Card (English/Pinyin) | Code in the CLI |
| :------------: | :-------------------: | :-------------: |
|       军旗      |  **ju**n **qi**       |       juqi      |
|       工兵      |  **go**ng **bi**n     |       gobi      |
|       排长      |  **pa**i **zh**ang    |       pazh      |
|       连长      |  **li**an **zh**ang   |       lizh      |
|       团长      |  **tu**an **zh**ang   |       tuzh      |
|       旅长      | lu (**lv**) **zh**ang |       lvzh      |
|       营长      |  **yi**ng **zh**ang   |       yizh      |
|       师长      |  **sh**i **zh**ang    |       shzh      |
|       军长      |  **ju**n **zh**ang    |       juzh      |
|       司令      |  **si** **li**ng      |       sili      |
|       炸弹      |  **zh**a **da**n      |       zhda      |
|       地雷      |  **di** **le**i       |       dile      |

### Rules, Sizes, and Setup

You can find out a lot more about specific rules, how to setup, and even how to "judge" pieces [here](https://baike.baidu.com/item/%E5%86%9B%E6%A3%8B/331209?fr=aladdin#:~:text=%E5%9C%B0%E9%9B%B7%E5%90%84%E4%B8%89%E3%80%82-,%E5%90%83%E5%AD%90%E8%A7%84%E5%88%99,-%E5%8F%B8%E4%BB%A4%3E%E5%86%9B%E9%95%BF).

## How to Use *Jun*

### Set up
`make jun`

## Start game
`make start`

