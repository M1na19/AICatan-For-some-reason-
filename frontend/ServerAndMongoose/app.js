var express = require("express"),
    mongoose = require("mongoose"),
    passport = require("passport"),
    bodyParser = require("body-parser"),
    LocalStrategy = require("passport-local"),
    passportLocalMongoose = require("passport-local-mongoose"),
    lpath = require('path'),
    proc = require('process'),
    fork = require('child_process'),
    cookieParser = require("cookie-parser");
const User = require("./model/User");
var app = express();
  
mongoose.connect("mongodb://localhost/27017");
  
app.set("view engine", "ejs");
app.use(bodyParser.urlencoded({ extended: true }));
app.use(require("express-session")({
    secret: "Rusty is a dog",
    resave: false,
    saveUninitialized: false
}));
  
app.use(passport.initialize());
app.use(passport.session());
app.use(cookieParser());
  
passport.use(new LocalStrategy(User.authenticate()));
passport.serializeUser(User.serializeUser());
passport.deserializeUser(User.deserializeUser());

// hopefully server python
//fork("python ../../backend/app.py", (in, out, err) => {})

//=====================
// ROUTES
//=====================
  
// Showing home page
app.get("/",async function (req, res) {
    let lb_users = (await User.aggregate([{$sort: {wins: -1}}])).slice(0, 10).map((x) => {return {username: x.username, wins: x.wins}});
    res.cookie("toppers", JSON.stringify(lb_users), {sameSite: "none", secure: true});
    res.render("home");
});

app.post("/endgame",async function (req, res) {
  await User.findOne({username: JSON.parse(req.cookies.user).username}).updateOne({},
      {$inc: {wins: req.body.wins, games: req.body.games, vps: req.body.vps}}).exec();
  console.log((await User.findOne({username: JSON.parse(req.cookies.user).username})).toJSON());
  let lb_users = (await User.aggregate([{$sort: {wins: -1}}])).slice(0, 10).map((x) => {return {username: x.username, wins: x.wins}});
  res.cookie("user", JSON.stringify((await User.findOne({username: JSON.parse(req.cookies.user).username})).toJSON()), {sameSite: "none", secure: true});
  res.cookie("toppers", JSON.stringify(lb_users), {sameSite: "none", secure: true});
  res.render("home");
});
  
// Showing secret page
app.get("/secret", isLoggedIn, function (req, res) {
    res.render("secret");
});
  
// Showing register form
app.get("/register", function (req, res) {
    res.render("register");
});

const mainfiles = [
  'styles/popup.css',
  'style.css',
  // 'main.html',
  'scripts/action.js',
  'scripts/buttonsListeners.js',
  'scripts/control.js',
  'scripts/features.js',
  'scripts/game.js',
  'scripts/piece.js',
  'scripts/UI.js',
  'images/background.png',
  'images/bricktile.png',
  'images/desert.png',
  'images/graintile.png',
  'images/hexagon.png',
  'images/oretile.png',
  'images/player.png',
  'images/rolling_dice.gif',
  'images/spotlight.png',
  'images/woodtile.png',
  'images/wooltile.png',
]

for (let path of mainfiles) {
  let type = path.match(/\.(.*)/)[1];
  type = type == 'css' ? 'text/css' :
          type == 'js' ? 'text/javascript' :
          type == 'gif' ? 'image/gif' :
          'image/png';
  app.get("/" + path, (_, res) => { res.setHeader('Content-Type', type); res.sendFile(lpath.join(__dirname, '../' + path)); });
}


app.get("/main", function (req, res) {
  // RULEAZA PYTHON
  res.sendFile(lpath.join(__dirname, '../main.html'));
});
  
// Handling user signup
app.post("/register", async (req, res) => {
    const user = await User.create({
      username: req.body.username,
      password: req.body.password,
      wins: 0,
      games: 0,
      vps: 0
    });
    
    return res.status(200).json(user);
  });
  
//Showing login form
app.get("/login", function (req, res) {
    res.render("login");
});
  
//Handling user login
app.post("/login", async function(req, res){
    try {
        // check if the user exists
        const user = await User.findOne({ username: req.body.username });
        if (user) {
          //check if password matches
          const result = req.body.password === user.password;
          if (result) {
            res.cookie("user", JSON.stringify(user), {sameSite: "none", secure: true});
            let lb_users = (await User.aggregate([{$sort: {wins: -1}}])).slice(0, 10).map((x) => {return {username: x.username, wins: x.wins}});
            res.cookie("toppers", JSON.stringify(lb_users), {sameSite: "none", secure: true});
            res.render("secret");
          } else {
            res.status(400).json({ error: "password doesn't match" });
          }
        } else {
          res.status(400).json({ error: "User doesn't exist" });
        }
      } catch (error) {
        res.status(400).json({ error });
      }
});
  
//Handling user logout 
app.get("/logout", function (req, res) {
    req.logout(function(err) {
        res.clearCookie("user");
        if (err) { return next(err); }
        res.redirect('/');
      });
});
  
function isLoggedIn(req, res, next) {
    if (req.isAuthenticated()) return next();
    res.redirect("/login");
}
  
var port = process.env.PORT || 3000;
app.listen(port, function () {
    console.log("Server Has Started!");
});

