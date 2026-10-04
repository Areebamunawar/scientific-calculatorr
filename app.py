import streamlit as st
import streamlit.components.v1 as components

st.set_page_config(page_title="Scientific Calculator | Areeba", page_icon="🧮",
                   layout="centered", initial_sidebar_state="collapsed")

st.markdown("""
<style>
#MainMenu, footer, header {visibility: hidden;}
.block-container {max-width: 600px; padding-top: 1.6rem; padding-bottom: 1rem;}
.title {font-size: 2rem; font-weight: 800; margin: 0;}
.subtitle {color: #8d97aa; margin: .1rem 0 1rem;}
.hint {font-size: .85rem; color: #8d97aa; margin-top: .6rem; text-align: center;}
</style>
""", unsafe_allow_html=True)

st.markdown('<div class="title">🧮 Scientific Calculator</div>', unsafe_allow_html=True)
st.markdown('<div class="subtitle">Created by <b>Areeba</b> · use the screen buttons or your keyboard</div>',
            unsafe_allow_html=True)

html = r"""
<!DOCTYPE html><html><head><meta charset="UTF-8">
<link href="https://fonts.googleapis.com/css2?family=Space+Grotesk:wght@400;500;700&display=swap" rel="stylesheet">
<style>
*{box-sizing:border-box}
body{margin:0;background:transparent;font-family:"Space Grotesk",Arial,sans-serif;color:#e8ecf3}
.calc{max-width:560px;margin:auto;padding:16px;border-radius:24px;background:#151a23;
  box-shadow:0 18px 44px rgba(0,0,0,.4);outline:none}
.display{background:#0b0e14;border-radius:16px;padding:12px 16px 14px;margin-bottom:12px;min-height:128px}
.badge{display:inline-block;font-size:12px;font-weight:700;color:#6fe0cb;background:#17353a;
  padding:2px 9px;border-radius:20px;cursor:pointer;border:0}
.expr{margin-top:6px;text-align:right;font-size:22px;color:#aab3c5;min-height:30px;
  white-space:nowrap;overflow-x:auto;scrollbar-width:none;font-variant-numeric:tabular-nums}
.res{text-align:right;font-size:44px;font-weight:700;min-height:56px;margin-top:4px;color:#f5b942;
  white-space:nowrap;overflow-x:auto;scrollbar-width:none;font-variant-numeric:tabular-nums}
.res.live{color:#6c7689}.res.err{color:#ff8a7d;font-size:24px;padding-top:12px}
.grid{display:grid;grid-template-columns:repeat(5,1fr);gap:8px}
.grid button{border:0;border-radius:14px;height:54px;font:600 18px "Space Grotesk",Arial,sans-serif;
  cursor:pointer;background:#222a37;color:#fff;transition:transform .07s,filter .07s}
.grid button:hover{filter:brightness(1.25)}
.grid button:active,.grid button.press{transform:scale(.94);filter:brightness(1.5)}
.fn{background:#17353a!important;color:#6fe0cb!important;font-size:16px!important}
.op{background:#2b3350!important;color:#aebdff!important;font-size:22px!important}
.clr{background:#3b2024!important;color:#ff8a7d!important}
.eq{background:#f5b942!important;color:#1a1405!important;font-size:24px!important}
.hist{margin-top:12px;background:#0b0e14;border-radius:16px;padding:10px 14px;max-height:118px;overflow:auto}
.hist h4{margin:0 0 6px;font-size:13px;font-weight:500;color:#8d97aa}
.item{font-size:14px;padding:5px 0;border-bottom:1px solid #1d2330;cursor:pointer;color:#aab3c5}
.item:last-child{border:0}.item:hover{color:#fff}.item b{color:#f5b942}
.empty{font-size:13px;color:#5d6678}
.foot{text-align:center;font-size:12px;color:#5d6678;margin-top:10px}
@media(max-width:420px){.grid button{height:48px;font-size:16px}.res{font-size:34px}.calc{padding:10px}}
</style></head><body>
<div class="calc" id="calc" tabindex="0">
  <div class="display">
    <button class="badge" id="mode" data-a="a:mode" title="Switch degrees / radians (D)">DEG</button>
    <div class="expr" id="expr">0</div>
    <div class="res live" id="res"></div>
  </div>
  <div class="grid">
    <button class="fn" data-a="f:sin(">sin</button><button class="fn" data-a="f:cos(">cos</button>
    <button class="fn" data-a="f:tan(">tan</button><button class="fn" data-a="f:(">(</button>
    <button class="fn" data-a="f:)">)</button>

    <button class="fn" data-a="f:asin(">sin⁻¹</button><button class="fn" data-a="f:acos(">cos⁻¹</button>
    <button class="fn" data-a="f:atan(">tan⁻¹</button><button class="fn" data-a="f:π">π</button>
    <button class="fn" data-a="f:e">e</button>

    <button class="fn" data-a="f:sinh(">sinh</button><button class="fn" data-a="f:cosh(">cosh</button>
    <button class="fn" data-a="f:tanh(">tanh</button><button class="fn" data-a="f:abs(">|x|</button>
    <button class="fn" data-a="f:Ans">Ans</button>

    <button class="fn" data-a="f:log(">log</button><button class="fn" data-a="f:ln(">ln</button>
    <button class="fn" data-a="f:√(">√</button><button class="fn" data-a="o:^2">x²</button>
    <button class="fn" data-a="o:^">xʸ</button>

    <button class="fn" data-a="o:^(-1)">1/x</button><button class="fn" data-a="o:!">n!</button>
    <button class="fn" data-a="o:%">%</button><button class="clr" data-a="a:back">⌫</button>
    <button class="clr" data-a="a:clear">AC</button>

    <button data-a="n:7">7</button><button data-a="n:8">8</button><button data-a="n:9">9</button>
    <button class="op" data-a="o:÷">÷</button><button class="op" data-a="o:×">×</button>

    <button data-a="n:4">4</button><button data-a="n:5">5</button><button data-a="n:6">6</button>
    <button class="op" data-a="o:−">−</button><button class="op" data-a="o:+">+</button>

    <button data-a="n:1">1</button><button data-a="n:2">2</button><button data-a="n:3">3</button>
    <button data-a="a:sign">±</button><button class="eq" data-a="a:eq" style="grid-row:span 2;height:auto">=</button>

    <button data-a="n:0" style="grid-column:span 2">0</button><button data-a="n:.">.</button>
    <button class="fn" data-a="f:,">,</button>
  </div>
  <div class="hist"><h4>History (tap to reuse)</h4><div id="hist"><div class="empty">No calculations yet</div></div></div>
  <div class="foot">Scientific Calculator · by Areeba</div>
</div>
<script>
(function(){
const $=id=>document.getElementById(id);
const exprEl=$("expr"),resEl=$("res"),histEl=$("hist"),modeEl=$("mode");
let expr="",deg=true,ans=0,done=false,hist=[];
const FN=["asin","acos","atan","sinh","cosh","tanh","sin","cos","tan","log","ln","abs"];
const TOK=/\d+\.?\d*|\.\d+|asin|acos|atan|sinh|cosh|tanh|sin|cos|tan|log|ln|abs|Ans|√|π|e|[+\-×÷^%!()−]/g;
const OPS="+−×÷^";
const R=x=>deg?x*Math.PI/180:x, A=x=>deg?x*180/Math.PI:x;
const fact=n=>{if(n<0||!Number.isInteger(n)||n>170)throw Error("Factorial needs a whole number 0–170");
  let r=1;for(let i=2;i<=n;i++)r*=i;return r;};
const env={
  sin:x=>Math.sin(R(x)),cos:x=>Math.cos(R(x)),
  tan:x=>{if(deg&&Math.abs(x%180)===90)throw Error("tan is undefined here");return Math.tan(R(x));},
  asin:x=>A(Math.asin(x)),acos:x=>A(Math.acos(x)),atan:x=>A(Math.atan(x)),
  sinh:Math.sinh,cosh:Math.cosh,tanh:Math.tanh,log10:Math.log10,ln:Math.log,
  sqrt:Math.sqrt,abs:Math.abs,fact:fact,PI:Math.PI,E:Math.E
};
function evaluate(src){
  let s=src.replace(/\s/g,"");
  const open=(s.match(/\(/g)||[]).length-(s.match(/\)/g)||[]).length;
  if(open<0)throw Error("Brackets don't match");
  s+=")".repeat(open);
  const t=s.match(TOK)||[];
  if(t.join("")!==s)throw Error("Invalid input");
  const val=x=>/^[\d.]/.test(x)||x==="π"||x==="e"||x==="Ans";
  const map={"×":"*","÷":"/","^":"**","π":"PI","e":"E","Ans":"("+ans+")","√":"sqrt","log":"log10","%":"/100"};
  let out="",prev="";
  for(const x of t){
    const start=val(x)||x==="("||x==="√"||FN.includes(x);
    const end=val(prev)||prev===")"||prev==="%"||prev==="!";
    if(prev&&end&&start)out+="*";
    if(x==="−"){
      const unary=!prev||OPS.includes(prev)||prev==="(";
      out+=!unary?"-":(prev==="^"?"-":"(-1)*");
    }else if(x==="+"&&(!prev||prev==="(")){/* unary plus */}
    else out+=(map[x]!==undefined?map[x]:x);
    prev=x;
  }
  const re=/(\d+\.?\d*|PI|E|\((?:[^()]|\((?:[^()]|\([^()]*\))*\))*\))!/;
  while(out.includes("!")){const n=out.replace(re,"fact($1)");if(n===out)throw Error("Invalid factorial");out=n;}
  let v;
  try{v=new Function(...Object.keys(env),'"use strict";return ('+out+')')(...Object.values(env));}
  catch(e){throw Error(e instanceof SyntaxError?"Invalid input":e.message);}
  if(typeof v!=="number"||isNaN(v))throw Error("Math error");
  if(!isFinite(v))throw Error("Cannot divide by zero / too large");
  return v;
}
function fmt(v){
  if(Math.abs(v)<1e-12)v=0;
  const a=Math.abs(v);
  if(a!==0&&(a>=1e15||a<1e-9))return v.toExponential(8).replace(/\.?0+e/,"e");
  return String(parseFloat(v.toPrecision(12)));
}
function render(err){
  exprEl.textContent=(expr||"0")+(done?" =":"");
  exprEl.scrollLeft=exprEl.scrollWidth;
  modeEl.textContent=deg?"DEG":"RAD";
  resEl.className="res";
  if(err){resEl.classList.add("err");resEl.textContent=err;return;}
  if(done){resEl.textContent=fmt(ans);return;}
  let p="";
  if(expr){try{p=fmt(evaluate(expr));}catch(e){p="";}}
  resEl.classList.add("live");
  resEl.textContent=(p&&p!==expr)?p:"";
}
function put(kind,s){
  if(done){
    if(kind==="o"){expr="Ans"+s;}else{expr=s;}
    done=false;render();return;
  }
  if(kind==="n"&&s==="."){
    const part=expr.split(/[^0-9.]/).pop();
    if(part.includes("."))return;
    if(!part)s="0.";
  }
  if(kind==="o"&&OPS.includes(s)&&s.length===1){
    const last=expr.slice(-1);
    if(!expr&&s!=="−"&&s!=="+")return;
    if(OPS.includes(last)&&!(s==="−"&&"×÷^".includes(last))){
      expr=expr.slice(0,-1);
      if(!expr&&s!=="−")return;
    }
  }
  if(kind==="o"&&(s==="%"||s==="!")&&!/[\d)πe]$|Ans$/.test(expr))return;
  expr+=s;render();
}
function act(a){
  const [k,v]=[a.slice(0,1),a.slice(2)];
  const btn=document.querySelector('[data-a="'+a.replace(/"/g,'\\"')+'"]');
  if(btn){btn.classList.add("press");setTimeout(()=>btn.classList.remove("press"),120);}
  if(k==="n"||k==="o"||k==="f"){put(k,v);return;}
  if(v==="clear"){expr="";done=false;render();}
  else if(v==="back"){
    if(done){done=false;}
    const m=expr.match(/(asin|acos|atan|sinh|cosh|tanh|sin|cos|tan|log|ln|abs|√)\($|Ans$/);
    expr=m?expr.slice(0,-m[0].length):expr.slice(0,-1);render();
  }
  else if(v==="mode"){deg=!deg;render();}
  else if(v==="sign"){
    if(done){expr="Ans";done=false;}
    if(!expr)expr="−";
    else if(expr.startsWith("−(")&&expr.endsWith(")"))expr=expr.slice(2,-1);
    else expr="−("+expr+")";
    render();
  }
  else if(v==="eq"){
    if(!expr||done)return;
    try{
      const r=evaluate(expr);ans=r;done=true;
      hist.unshift({e:expr,r:fmt(r)});hist=hist.slice(0,10);
      histEl.innerHTML=hist.map((h,i)=>'<div class="item" data-i="'+i+'">'+h.e+' = <b>'+h.r+'</b></div>').join("");
      render();
    }catch(e){render(e.message||"Invalid input");}
  }
}
function keyToAction(e){
  const k=e.key;
  if(/^[0-9.]$/.test(k))return "n:"+k;
  const m={"+":"o:+","-":"o:−","*":"o:×","x":"o:×","X":"o:×","/":"o:÷","^":"o:^","%":"o:%","!":"o:!",
    "(":"f:(",")":"f:)",",":"f:,","Enter":"a:eq","=":"a:eq","Backspace":"a:back","Escape":"a:clear","Delete":"a:clear",
    "s":"f:sin(","c":"f:cos(","t":"f:tan(","l":"f:log(","n":"f:ln(","r":"f:√(","p":"f:π","e":"f:e","a":"f:Ans",
    "d":"a:mode","q":"o:^2","i":"o:^(-1)"};
  return m[k]||null;
}
function onKey(e){
  if(e.ctrlKey||e.metaKey||e.altKey)return;
  const a=keyToAction(e);
  if(a){e.preventDefault();act(a);}
}
document.querySelectorAll("button[data-a]").forEach(b=>b.addEventListener("click",()=>{act(b.dataset.a);b.blur();}));
histEl.addEventListener("click",e=>{
  const it=e.target.closest(".item");
  if(it){expr=hist[+it.dataset.i].e;done=false;render();}
});
document.addEventListener("keydown",onKey);
try{ // also listen on the Streamlit page so typing works without clicking the calculator first
  const pw=window.parent;
  if(pw.__calcKey)pw.document.removeEventListener("keydown",pw.__calcKey);
  pw.__calcKey=onKey;pw.document.addEventListener("keydown",onKey);
}catch(_){}
$("calc").focus();render();
})();
</script></body></html>
"""

components.html(html, height=900, scrolling=False)

st.markdown(
    '<div class="hint">Keyboard: 0–9 · + − * / ^ · ( ) · % · ! · Enter = · Backspace · Esc = clear<br>'
    'Shortcuts: s sin · c cos · t tan · l log · n ln · r √ · p π · e · a Ans · q x² · i 1/x · d DEG/RAD</div>',
    unsafe_allow_html=True)
