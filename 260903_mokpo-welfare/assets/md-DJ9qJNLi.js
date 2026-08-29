import{f as y,O as A,G as L,o as g,e as k,j as u,g as n,aa as d,r as P,b as R,w as T,d as C,v as F,x as G,C as x}from"./modules/vue-Cy6YmmWd.js";import{u as _,f as E}from"./slidev/context-CBwH2Y1N.js";import{_ as B}from"./index-CJ5s8rBc.js";import{I}from"./slidev/default-8PKUr8Nb.js";import"./modules/shiki-4ebWkmc9.js";const N={class:"absolute inset-0 w-full h-full flex flex-col justify-between select-none overflow-hidden bg-black p-12 px-14 text-left font-['Nanum_Gothic',sans-serif]"},z=`
  attribute vec2 position;
  void main() {
    gl_Position = vec4(position, 0.0, 1.0);
  }
`,D=`
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
`,U=y({__name:"CoverSlide",setup(b){_();const o=P(null);let s=null,e=null,r=null,c=null,f=null,w=Date.now();function v(t,a,l){const i=t.createShader(a);return i?(t.shaderSource(i,l),t.compileShader(i),t.getShaderParameter(i,t.COMPILE_STATUS)?i:(console.error("Shader compile error:",t.getShaderInfoLog(i)),t.deleteShader(i),null)):null}function S(){const t=o.value;if(!t||(e=t.getContext("webgl",{antialias:!0,alpha:!1}),!e))return;const a=v(e,e.VERTEX_SHADER,z),l=v(e,e.FRAGMENT_SHADER,D);if(!a||!l||(r=e.createProgram(),!r))return;if(e.attachShader(r,a),e.attachShader(r,l),e.linkProgram(r),!e.getProgramParameter(r,e.LINK_STATUS)){console.error("Program link error:",e.getProgramInfoLog(r));return}e.useProgram(r);const i=e.createBuffer();e.bindBuffer(e.ARRAY_BUFFER,i),e.bufferData(e.ARRAY_BUFFER,new Float32Array([-1,-1,1,-1,-1,1,-1,1,1,-1,1,1]),e.STATIC_DRAW);const h=e.getAttribLocation(r,"position");e.enableVertexAttribArray(h),e.vertexAttribPointer(h,2,e.FLOAT,!1,0,0),c=e.getUniformLocation(r,"u_time"),f=e.getUniformLocation(r,"u_resolution"),m(),p()}function m(){if(!o.value||!e)return;const t=o.value.clientWidth||980,a=o.value.clientHeight||552,l=Math.min(window.devicePixelRatio||1,2);o.value.width=t*l,o.value.height=a*l,e.viewport(0,0,o.value.width,o.value.height)}function p(){if(!e||!r)return;const t=(Date.now()-w)/1e3;c&&e.uniform1f(c,t),f&&o.value&&e.uniform2f(f,o.value.width,o.value.height),e.drawArrays(e.TRIANGLES,0,6),s=requestAnimationFrame(p)}return A(()=>{S(),window.addEventListener("resize",m)}),L(()=>{s&&cancelAnimationFrame(s),window.removeEventListener("resize",m)}),(t,a)=>(g(),k("div",N,[u(" ── Continuous Moving WebGL Fluid Canvas with Silky Smooth Natural Gradient ── "),n("canvas",{ref_key:"canvasRef",ref:o,class:"absolute inset-0 w-full h-full block pointer-events-none"},null,512),u(" ── Top Tag ── "),a[0]||(a[0]=n("div",{class:"relative z-10"},[n("span",{class:"inline-block text-xs md:text-sm font-bold tracking-widest text-white uppercase pure-white-text"}," 2026 사회서비스 종사자 디지털 교육 ")],-1)),u(" ── Center: Apple Keynote Statement Layout (100% Pure White Floating Title) ── "),a[1]||(a[1]=n("div",{class:"relative z-10 my-auto max-w-3xl space-y-4 pt-2"},[n("h1",{class:"text-4xl md:text-[54px] font-extrabold leading-[1.2] tracking-tight pure-white-title"},[d(" AI를 활용한"),n("br"),d(" 문서 작성 협업 역량 강화 ")]),n("p",{class:"text-sm md:text-base font-normal leading-relaxed max-w-xl pure-white-sub"}," 생성형 AI의 작동 원리부터 실무 표준 지시, 도구 협업, 나만의 스킬 자산화까지 ")],-1)),u(" ── Bottom Bar: Right-Aligned Presenter Text (오진실 강사) ── "),a[2]||(a[2]=n("div",{class:"relative z-10 flex items-center justify-between border-t border-white/20 pt-4"},[n("span",{class:"text-xs text-white/70 font-medium pure-white-text"}," 목포종합사회복지관 "),n("span",{class:"text-sm md:text-base font-bold text-white tracking-wide flex items-center gap-2 pure-white-text"},[n("span",{class:"text-white/60 font-normal text-xs uppercase tracking-widest"},"Presenter"),d(" 오진실 강사 ")])],-1))]))}}),V=B(U,[["__scopeId","data-v-4d3a9670"]]),O={__name:"slides.md__slidev_1",setup(b){const{$clicksContext:o,$frontmatter:s}=_();return o.setup(),(e,r)=>{const c=V;return g(),R(I,F(G(x(E)(x(s),0))),{default:T(()=>[u(" slide:1 "),C(c)]),_:1},16)}}};export{O as default};
