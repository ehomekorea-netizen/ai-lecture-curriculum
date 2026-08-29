import{f as y,O as P,G as R,o as p,e as S,j as f,g as i,aa as v,r as C,i as L,k as T,z as F,b as G,w as B,d as E,v as N,x as z,C as b}from"./modules/vue-D7EkmRMR.js";import{u as h,f as I}from"./slidev/context-yujdEyiV.js";import{_ as U}from"./index-B41COPWj.js";import"./modules/shiki-B3tbO57W.js";const $={class:"absolute inset-0 w-full h-full flex flex-col justify-between select-none overflow-hidden bg-black p-12 px-14 text-left font-['Nanum_Gothic',sans-serif]"},D=`
  attribute vec2 position;
  void main() {
    gl_Position = vec4(position, 0.0, 1.0);
  }
`,V=`
  precision highp float;
  uniform vec2 u_resolution;
  uniform float u_time;

  float hash(vec2 p) {
    return fract(sin(dot(p, vec2(127.1, 311.7))) * 43758.5453123);
  }

  float noise(vec2 p) {
    vec2 i = floor(p);
    vec2 f = fract(p);
    f = f * f * (3.0 - 2.0 * f);
    return mix(mix(hash(i + vec2(0.0, 0.0)), hash(i + vec2(1.0, 0.0)), f.x),
               mix(hash(i + vec2(0.0, 1.0)), hash(i + vec2(1.0, 1.0)), f.x), f.y);
  }

  float fbm(vec2 p) {
    float v = 0.0;
    float a = 0.5;
    mat2 rot = mat2(cos(0.55), sin(0.55), -sin(0.55), cos(0.55));
    for (int i = 0; i < 5; ++i) {
      v += a * noise(p);
      p = rot * p * 2.1 + vec2(80.0);
      a *= 0.5;
    }
    return v;
  }

  void main() {
    vec2 uv = gl_FragCoord.xy / u_resolution.xy;
    vec2 p = (gl_FragCoord.xy - 0.5 * u_resolution.xy) / u_resolution.y;

    // Smooth dynamic fluid motion
    float t = u_time * 0.32;
    
    // Dynamic multi-layer turbulent organic fluid flow
    vec2 q = vec2(fbm(p + vec2(t * 0.42, t * 0.26)), fbm(p + vec2(t * 0.30, -t * 0.20)));
    vec2 r = vec2(fbm(p + 3.2 * q + vec2(1.7, 9.2) + 0.22 * t), fbm(p + 3.2 * q + vec2(8.3, 2.8) + 0.16 * t));
    float f = fbm(p + 4.2 * r);

    // ── Silky Smooth Natural Gradient (Calm comfortable navy on left -> Luminous cobalt on right) ──
    float lightGrad = smoothstep(0.02, 0.95, uv.x);

    vec3 calmNavy = vec3(0.02, 0.04, 0.11);
    vec3 midCobalt = vec3(0.07, 0.22, 0.62);
    vec3 brightCyan = vec3(0.18, 0.58, 0.98);
    vec3 peakGlow = vec3(0.48, 0.85, 1.0);

    vec3 col = mix(calmNavy, midCobalt, clamp((f * f) * 3.4, 0.0, 1.0));
    col = mix(col, brightCyan, clamp(length(q) * (0.35 + 0.65 * lightGrad), 0.0, 1.0));
    col = mix(col, peakGlow, clamp(length(r.x) * lightGrad * 0.55, 0.0, 1.0));

    // Eye-friendly natural lighting transition (Comfortable on eyes, zero harsh boundaries)
    col = mix(col * 0.72, col * 1.08, lightGrad);

    gl_FragColor = vec4(col, 1.0);
  }
`,W=y({__name:"CoverSlide",setup(r){h();const t=C(null);let l=null,e=null,o=null,u=null,m=null,A=Date.now();function g(a,n,c){const s=a.createShader(n);return s?(a.shaderSource(s,c),a.compileShader(s),a.getShaderParameter(s,a.COMPILE_STATUS)?s:(console.error("Shader compile error:",a.getShaderInfoLog(s)),a.deleteShader(s),null)):null}function k(){const a=t.value;if(!a||(e=a.getContext("webgl",{antialias:!0,alpha:!1}),!e))return;const n=g(e,e.VERTEX_SHADER,D),c=g(e,e.FRAGMENT_SHADER,V);if(!n||!c||(o=e.createProgram(),!o))return;if(e.attachShader(o,n),e.attachShader(o,c),e.linkProgram(o),!e.getProgramParameter(o,e.LINK_STATUS)){console.error("Program link error:",e.getProgramInfoLog(o));return}e.useProgram(o);const s=e.createBuffer();e.bindBuffer(e.ARRAY_BUFFER,s),e.bufferData(e.ARRAY_BUFFER,new Float32Array([-1,-1,1,-1,-1,1,-1,1,1,-1,1,1]),e.STATIC_DRAW);const _=e.getAttribLocation(o,"position");e.enableVertexAttribArray(_),e.vertexAttribPointer(_,2,e.FLOAT,!1,0,0),u=e.getUniformLocation(o,"u_time"),m=e.getUniformLocation(o,"u_resolution"),d(),x()}function d(){if(!t.value||!e)return;const a=t.value.clientWidth||980,n=t.value.clientHeight||552,c=Math.min(window.devicePixelRatio||1,2);t.value.width=a*c,t.value.height=n*c,e.viewport(0,0,t.value.width,t.value.height)}function x(){if(!e||!o)return;const a=(Date.now()-A)/1e3;u&&e.uniform1f(u,a),m&&t.value&&e.uniform2f(m,t.value.width,t.value.height),e.drawArrays(e.TRIANGLES,0,6),l=requestAnimationFrame(x)}return P(()=>{k(),window.addEventListener("resize",d)}),R(()=>{l&&cancelAnimationFrame(l),window.removeEventListener("resize",d)}),(a,n)=>(p(),S("div",$,[f(" ── Continuous Moving WebGL Fluid Canvas with Silky Smooth Natural Gradient ── "),i("canvas",{ref_key:"canvasRef",ref:t,class:"absolute inset-0 w-full h-full block pointer-events-none"},null,512),f(" ── Top Tag ── "),n[0]||(n[0]=i("div",{class:"relative z-10"},[i("span",{class:"inline-block text-xs md:text-sm font-bold tracking-widest text-white uppercase pure-white-text"}," 2026 사회서비스 종사자 디지털 교육 ")],-1)),f(" ── Center: Apple Keynote Statement Layout (100% Pure White Floating Title) ── "),n[1]||(n[1]=i("div",{class:"relative z-10 my-auto max-w-3xl space-y-4 pt-2"},[i("h1",{class:"text-4xl md:text-[54px] font-extrabold leading-[1.2] tracking-tight pure-white-title"},[v(" AI를 활용한"),i("br"),v(" 문서 작성 협업 역량 강화 ")]),i("p",{class:"text-sm md:text-base font-normal leading-relaxed max-w-xl pure-white-sub"}," 생성형 AI의 작동 원리부터 실무 표준 지시, 도구 협업, 나만의 스킬 자산화까지 ")],-1)),f(" ── Bottom Bar: Right-Aligned Presenter Text (오진실 강사) ── "),n[2]||(n[2]=i("div",{class:"relative z-10 flex items-center justify-between border-t border-white/20 pt-4"},[i("span",{class:"text-xs text-white/70 font-medium pure-white-text"}," 목포종합사회복지관 "),i("span",{class:"text-sm md:text-base font-bold text-white tracking-wide flex items-center gap-2 pure-white-text"},[i("span",{class:"text-white/60 font-normal text-xs uppercase tracking-widest"},"Presenter"),v(" 오진실 강사 ")])],-1))]))}}),q=U(W,[["__scopeId","data-v-4d3a9670"]]);function w(r){return r.startsWith("/")?"/260903_mokpo-welfare/"+r.slice(1):r}function M(r,t=!1){const l=r&&["#","rgb","hsl"].some(o=>r.indexOf(o)===0),e={background:l?r:void 0,color:r&&!l?"white":void 0,backgroundImage:l?void 0:r?t?`linear-gradient(#0005, #0008), url(${w(r)})`:`url("${w(r)}")`:void 0,backgroundRepeat:"no-repeat",backgroundPosition:"center",backgroundSize:"cover"};return e.background||delete e.background,e}const O={class:"my-auto w-full"},j=y({__name:"cover",props:{background:{default:""}},setup(r){h();const t=r,l=F(()=>M(t.background,!0));return(e,o)=>(p(),S("div",{class:"slidev-layout cover",style:T(l.value)},[i("div",O,[L(e.$slots,"default")])],4))}}),J={__name:"slides.md__slidev_1",setup(r){const{$clicksContext:t,$frontmatter:l}=h();return t.setup(),(e,o)=>{const u=q;return p(),G(j,N(z(b(I)(b(l),0))),{default:B(()=>[f(" slide:1 "),E(u)]),_:1},16)}}};export{J as default};
