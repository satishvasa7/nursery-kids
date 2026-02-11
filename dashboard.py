from flask import Flask, render_template_string

app = Flask(__name__)

# HTML template with two tabs
template = """
<!DOCTYPE html>
<html>
<head>
    <title>Nursery Kids Dashboard</title>
    <style>
        body { 
            font-family: 'Comic Sans MS', 'Arial Rounded MT Bold', cursive; 
            background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
            margin: 0;
            padding: 20px;
        }
        .header {
            text-align: center;
            color: white;
            margin-bottom: 20px;
        }
        .header img {
            max-width: 300px;
            width: 100%;
            border-radius: 15px;
            box-shadow: 0 4px 6px rgba(0,0,0,0.3);
            margin-bottom: 20px;
        }
        h1 {
            font-size: 3em;
            text-shadow: 2px 2px 4px rgba(0,0,0,0.3);
            margin: 10px 0;
        }
        .tabs { 
            display: flex; 
            gap: 20px; 
            margin-bottom: 30px;
            justify-content: center;
            flex-wrap: wrap;
        }
        .tab { 
            padding: 15px 30px;
            cursor: pointer; 
            font-weight: bold;
            font-size: 1.2em;
            border: 3px solid white;
            border-radius: 10px;
            background-color: rgba(255,255,255,0.2);
            color: white;
            transition: all 0.3s ease;
        }
        .tab:hover {
            background-color: white;
            color: #667eea;
            transform: scale(1.05);
        }
        .content { display: none; }
        .active { display: block; }
        .items-grid {
            display: grid;
            grid-template-columns: repeat(auto-fit, minmax(120px, 1fr));
            gap: 15px;
            max-width: 1200px;
            margin: 0 auto;
        }
        .item {
            padding: 20px;
            border-radius: 10px;
            text-align: center;
            font-weight: bold;
            color: white;
            font-size: 1.1em;
            box-shadow: 0 4px 8px rgba(0,0,0,0.2);
            transition: transform 0.2s;
            cursor: pointer;
        }
        .item:hover {
            transform: scale(1.1);
        }
        .item-image {
            font-size: 3em;
            margin-bottom: 10px;
        }
    </style>
    <script>
        function showTab(tabId) {
            document.getElementById('alphabets').style.display = 'none';
            document.getElementById('numbers').style.display = 'none';
            document.getElementById(tabId).style.display = 'block';
        }
    </script>
</head>
<body>
    <div class="header">
        <img src="https://images.unsplash.com/photo-1503454537688-e6753770b1c5?w=400&h=300&fit=crop" alt="Happy Kids">
        <h1>🎨 Nursery Kids Dashboard 🎨</h1>
        <p style="font-size: 1.3em;">Learn Numbers and Alphabets with Colors!</p>
    </div>

    <div class="tabs">
        <div class="tab" onclick="showTab('numbers')">Numbers (1-20)</div>
        <div class="tab" onclick="showTab('alphabets')">Alphabets (A-Z)</div>
    </div>

    <div id="numbers" class="content active">
        <h2 style="text-align: center; color: white; font-size: 2em;">Numbers 1 to 20</h2>
        <div class="items-grid">
            <div class="item" style="background-color: #FF6B6B;">1<br><small>One</small></div>
            <div class="item" style="background-color: #FF8E53;">2<br><small>Two</small></div>
            <div class="item" style="background-color: #FFC93C;">3<br><small>Three</small></div>
            <div class="item" style="background-color: #95E1D3;">4<br><small>Four</small></div>
            <div class="item" style="background-color: #64B5F6;">5<br><small>Five</small></div>
            <div class="item" style="background-color: #9575CD;">6<br><small>Six</small></div>
            <div class="item" style="background-color: #F06292;">7<br><small>Seven</small></div>
            <div class="item" style="background-color: #00BCD4;">8<br><small>Eight</small></div>
            <div class="item" style="background-color: #81C784;">9<br><small>Nine</small></div>
            <div class="item" style="background-color: #FFB74D;">10<br><small>Ten</small></div>
            <div class="item" style="background-color: #E57373;">11<br><small>Eleven</small></div>
            <div class="item" style="background-color: #BA68C8;">12<br><small>Twelve</small></div>
            <div class="item" style="background-color: #26A69A;">13<br><small>Thirteen</small></div>
            <div class="item" style="background-color: #FF7043;">14<br><small>Fourteen</small></div>
            <div class="item" style="background-color: #5C6BC0;">15<br><small>Fifteen</small></div>
            <div class="item" style="background-color: #FFA726;">16<br><small>Sixteen</small></div>
            <div class="item" style="background-color: #AB47BC;">17<br><small>Seventeen</small></div>
            <div class="item" style="background-color: #29B6F6;">18<br><small>Eighteen</small></div>
            <div class="item" style="background-color: #66BB6A;">19<br><small>Nineteen</small></div>
            <div class="item" style="background-color: #EC407A;">20<br><small>Twenty</small></div>
        </div>
    </div>

    <div id="alphabets" class="content">
        <h2 style="text-align: center; color: white; font-size: 2em;">Alphabets A to Z</h2>
        <div class="items-grid">
            <div class="item" style="background-color: #FF6B6B;"><div class="item-image">🍎</div>A<br><small>Apple</small></div>
            <div class="item" style="background-color: #FF8E53;"><div class="item-image">🔴</div>B<br><small>Ball</small></div>
            <div class="item" style="background-color: #FFC93C;"><div class="item-image">🐱</div>C<br><small>Cat</small></div>
            <div class="item" style="background-color: #95E1D3;"><div class="item-image">🐕</div>D<br><small>Dog</small></div>
            <div class="item" style="background-color: #64B5F6;"><div class="item-image">🐘</div>E<br><small>Elephant</small></div>
            <div class="item" style="background-color: #9575CD;"><div class="item-image">🐠</div>F<br><small>Fish</small></div>
            <div class="item" style="background-color: #F06292;"><div class="item-image">🐐</div>G<br><small>Goat</small></div>
            <div class="item" style="background-color: #00BCD4;"><div class="item-image">🎩</div>H<br><small>Hat</small></div>
            <div class="item" style="background-color: #81C784;"><div class="item-image">🧊</div>I<br><small>Ice</small></div>
            <div class="item" style="background-color: #FFB74D;"><div class="item-image">🫖</div>J<br><small>Jug</small></div>
            <div class="item" style="background-color: #E57373;"><div class="item-image">🪁</div>K<br><small>Kite</small></div>
            <div class="item" style="background-color: #BA68C8;"><div class="item-image">🦁</div>L<br><small>Lion</small></div>
            <div class="item" style="background-color: #26A69A;"><div class="item-image">🐵</div>M<br><small>Monkey</small></div>
            <div class="item" style="background-color: #FF7043;"><div class="item-image">🪺</div>N<br><small>Nest</small></div>
            <div class="item" style="background-color: #5C6BC0;"><div class="item-image">🍊</div>O<br><small>Orange</small></div>
            <div class="item" style="background-color: #FFA726;"><div class="item-image">🦜</div>P<br><small>Parrot</small></div>
            <div class="item" style="background-color: #AB47BC;"><div class="item-image">👑</div>Q<br><small>Queen</small></div>
            <div class="item" style="background-color: #29B6F6;"><div class="item-image">🐰</div>R<br><small>Rabbit</small></div>
            <div class="item" style="background-color: #66BB6A;"><div class="item-image">☀️</div>S<br><small>Sun</small></div>
            <div class="item" style="background-color: #EC407A;"><div class="item-image">🐯</div>T<br><small>Tiger</small></div>
            <div class="item" style="background-color: #78909C;"><div class="item-image">☔</div>U<br><small>Umbrella</small></div>
            <div class="item" style="background-color: #A1887F;"><div class="item-image">🚐</div>V<br><small>Van</small></div>
            <div class="item" style="background-color: #FFC93C;"><div class="item-image">⌚</div>W<br><small>Watch</small></div>
            <div class="item" style="background-color: #FFD54F;"><div class="item-image">🎺</div>X<br><small>Xylophone</small></div>
            <div class="item" style="background-color: #BDBB49;"><div class="item-image">🐂</div>Y<br><small>Yak</small></div>
            <div class="item" style="background-color: #8D6E63;"><div class="item-image">🦓</div>Z<br><small>Zebra</small></div>
        </div>
    </div>
</body>
</html>
"""

@app.route("/")
def home():
    return render_template_string(template)

if __name__ == "__main__":
    # Run on port 4200, accessible externally
    app.run(host="0.0.0.0", port=4200)