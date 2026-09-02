import{f as y,O as A,G as F,o as _,e as E,j as i,g as a,aa as m,n as L,r as p,b as R,w as C,d as T,v as k,x as P,C as g}from"./modules/vue-Cy6YmmWd.js";import{u as b,f as G}from"./slidev/context-CT9Tezro.js";import{_ as N}from"./index-C1OFT0ml.js";import{I as B}from"./slidev/default-BPED27i0.js";import"./modules/shiki-4ebWkmc9.js";const I={class:"absolute inset-0 w-full h-full flex flex-col justify-center items-center select-none overflow-hidden bg-slate-950 p-10 px-12 text-center font-['Nanum_Gothic',sans-serif]"},V=`
  attribute vec2 position;
  void main() {
    gl_Position = vec4(position, 0.0, 1.0);
  }
`,q=`
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

    float t = u_time * 0.32;
    
    vec2 q = vec2(fbm(p + vec2(t * 0.42, t * 0.26)), fbm(p + vec2(t * 0.30, -t * 0.20)));
    vec2 r = vec2(fbm(p + 3.2 * q + vec2(1.7, 9.2) + 0.22 * t), fbm(p + 3.2 * q + vec2(8.3, 2.8) + 0.16 * t));
    float f = fbm(p + 4.2 * r);

    // Silky natural gradient
    float lightGrad = smoothstep(0.02, 0.95, uv.x);

    vec3 calmNavy = vec3(0.02, 0.04, 0.11);
    vec3 midCobalt = vec3(0.07, 0.22, 0.62);
    vec3 brightCyan = vec3(0.18, 0.58, 0.98);
    vec3 peakGlow = vec3(0.48, 0.85, 1.0);

    vec3 col = mix(calmNavy, midCobalt, clamp((f * f) * 3.4, 0.0, 1.0));
    col = mix(col, brightCyan, clamp(length(q) * (0.35 + 0.65 * lightGrad), 0.0, 1.0));
    col = mix(col, peakGlow, clamp(length(r.x) * lightGrad * 0.55, 0.0, 1.0));

    col = mix(col * 0.72, col * 1.08, lightGrad);

    gl_FragColor = vec4(col, 1.0);
  }
`,D=y({__name:"EndingSlide",setup(w){b();const h=p(null);let M=null,e=null,t=null,H=null,n=null,x=Date.now();const c=p(!1);let l=null;function u(v,o,z){const r=v.createShader(o);return r?(v.shaderSource(r,z),v.compileShader(r),v.getShaderParameter(r,v.COMPILE_STATUS)?r:(console.error("Shader compile error:",v.getShaderInfoLog(r)),v.deleteShader(r),null)):null}function S(){const v=h.value;if(!v||(e=v.getContext("webgl",{antialias:!0,alpha:!1}),!e))return;const o=u(e,e.VERTEX_SHADER,V),z=u(e,e.FRAGMENT_SHADER,q);if(!o||!z||(t=e.createProgram(),!t))return;if(e.attachShader(t,o),e.attachShader(t,z),e.linkProgram(t),!e.getProgramParameter(t,e.LINK_STATUS)){console.error("Program link error:",e.getProgramInfoLog(t));return}e.useProgram(t);const r=e.createBuffer();e.bindBuffer(e.ARRAY_BUFFER,r),e.bufferData(e.ARRAY_BUFFER,new Float32Array([-1,-1,1,-1,-1,1,-1,1,1,-1,1,1]),e.STATIC_DRAW);const d=e.getAttribLocation(t,"position");e.enableVertexAttribArray(d),e.vertexAttribPointer(d,2,e.FLOAT,!1,0,0),H=e.getUniformLocation(t,"u_time"),n=e.getUniformLocation(t,"u_resolution"),s(),f()}function s(){if(!h.value||!e)return;const v=h.value.clientWidth||980,o=h.value.clientHeight||552,z=Math.min(window.devicePixelRatio||1,2);h.value.width=v*z,h.value.height=o*z,e.viewport(0,0,h.value.width,h.value.height)}function f(){if(!e||!t)return;const v=(Date.now()-x)/1e3;H&&e.uniform1f(H,v),n&&h.value&&e.uniform2f(n,h.value.width,h.value.height),e.drawArrays(e.TRIANGLES,0,6),M=requestAnimationFrame(f)}return A(()=>{S(),window.addEventListener("resize",s),l=setTimeout(()=>{c.value=!0},5e3)}),F(()=>{M&&cancelAnimationFrame(M),l&&clearTimeout(l),window.removeEventListener("resize",s)}),(v,o)=>(_(),E("div",I,[i(" ── Continuous Moving WebGL Fluid Canvas with Silky Smooth Natural Gradient ── "),a("canvas",{ref_key:"canvasRef",ref:h,class:"absolute inset-0 w-full h-full block pointer-events-none"},null,512),i(" ── Center: Elegant 1.5x Statement Layout ── "),o[1]||(o[1]=a("div",{class:"relative z-10 my-auto w-full max-w-4xl space-y-6 px-4"},[a("div",{class:"pure-white-title break-keep"},[m(" AI는 초안을 쓰고,"),a("br"),m(" 가치는 여러분이 담습니다. ")]),a("div",{class:"pure-white-sub"}," 경청해 주셔서 감사합니다. ")],-1)),i(" ── 5s Delayed Slide-in: Free-Floating New QR Code (Exact qrcode.svg Vector) ── "),a("div",{class:L(["absolute bottom-6 left-8 z-20 transition-all duration-800 ease-out",c.value?"opacity-100 translate-y-0 scale-100 pointer-events-auto":"opacity-0 translate-y-8 scale-90 pointer-events-none"])},[i(" Crisp Vector SVG Floating Over Fluid Canvas with Soft Elevation "),o[0]||(o[0]=a("div",{class:"relative p-2 bg-white rounded-2xl shadow-[0_8px_32px_rgba(0,0,0,0.85)] border border-white/20"},[a("svg",{viewBox:"0 0 29 29",width:"152",height:"152","shape-rendering":"crispEdges",class:"block rounded-lg"},[a("path",{fill:"#FFFFFF",d:"M0,0 h29v29H0z"}),a("path",{fill:"#000000",d:"M0 0h7v1H0zM10 0h2v1H10zM14 0h1v1H14zM16 0h1v1H16zM19 0h2v1H19zM22,0 h7v1H22zM0 1h1v1H0zM6 1h1v1H6zM9 1h1v1H9zM12 1h1v1H12zM14 1h2v1H14zM17 1h2v1H17zM20 1h1v1H20zM22 1h1v1H22zM28,1 h1v1H28zM0 2h1v1H0zM2 2h3v1H2zM6 2h1v1H6zM8 2h4v1H8zM15 2h2v1H15zM19 2h1v1H19zM22 2h1v1H22zM24 2h3v1H24zM28,2 h1v1H28zM0 3h1v1H0zM2 3h3v1H2zM6 3h1v1H6zM8 3h1v1H8zM10 3h4v1H10zM15 3h3v1H15zM20 3h1v1H20zM22 3h1v1H22zM24 3h3v1H24zM28,3 h1v1H28zM0 4h1v1H0zM2 4h3v1H2zM6 4h1v1H6zM8 4h3v1H8zM12 4h2v1H12zM16 4h1v1H16zM18 4h3v1H18zM22 4h1v1H22zM24 4h3v1H24zM28,4 h1v1H28zM0 5h1v1H0zM6 5h1v1H6zM8 5h1v1H8zM10 5h1v1H10zM13 5h4v1H13zM22 5h1v1H22zM28,5 h1v1H28zM0 6h7v1H0zM8 6h1v1H8zM10 6h1v1H10zM12 6h1v1H12zM14 6h1v1H14zM16 6h1v1H16zM18 6h1v1H18zM20 6h1v1H20zM22,6 h7v1H22zM8 7h2v1H8zM11 7h1v1H11zM15 7h1v1H15zM0 8h1v1H0zM2 8h5v1H2zM10 8h2v1H10zM13 8h2v1H13zM17 8h1v1H17zM19 8h1v1H19zM22 8h5v1H22zM0 9h1v1H0zM3 9h1v1H3zM7 9h3v1H7zM13 9h1v1H13zM16 9h7v1H16zM24 9h1v1H24zM28,9 h1v1H28zM0 10h1v1H0zM3 10h2v1H3zM6 10h1v1H6zM9 10h1v1H9zM11 10h1v1H11zM14 10h2v1H14zM20 10h1v1H20zM22 10h1v1H22zM24 10h1v1H24zM1 11h1v1H1zM3 11h1v1H3zM7 11h4v1H7zM12 11h1v1H12zM15 11h2v1H15zM19 11h7v1H19zM27 11h1v1H27zM1 12h1v1H1zM3 12h1v1H3zM5 12h2v1H5zM8 12h2v1H8zM11 12h1v1H11zM13 12h2v1H13zM17 12h3v1H17zM23 12h1v1H23zM25 12h2v1H25zM1 13h2v1H1zM5 13h1v1H5zM7 13h1v1H7zM9 13h6v1H9zM16 13h2v1H16zM19 13h6v1H19zM28,13 h1v1H28zM0 14h4v1H0zM5 14h2v1H5zM8 14h1v1H8zM11 14h1v1H11zM15 14h1v1H15zM17 14h1v1H17zM22 14h1v1H22zM24 14h3v1H24zM0 15h2v1H0zM7 15h2v1H7zM12 15h1v1H12zM14 15h1v1H14zM16 15h1v1H16zM19 15h3v1H19zM23 15h2v1H23zM27 15h1v1H27zM0 16h1v1H0zM2 16h7v1H2zM10 16h3v1H10zM17 16h1v1H17zM19 16h1v1H19zM23 16h1v1H23zM25 16h2v1H25zM0 17h4v1H0zM7 17h1v1H7zM11 17h3v1H11zM19 17h1v1H19zM22 17h3v1H22zM26 17h1v1H26zM28,17 h1v1H28zM0 18h1v1H0zM2 18h5v1H2zM12 18h4v1H12zM17 18h2v1H17zM20 18h5v1H20zM26 18h1v1H26zM0 19h1v1H0zM4 19h2v1H4zM7 19h3v1H7zM11 19h1v1H11zM13 19h1v1H13zM18 19h1v1H18zM27 19h1v1H27zM0 20h1v1H0zM2 20h1v1H2zM5 20h3v1H5zM9 20h4v1H9zM14 20h4v1H14zM19 20h6v1H19zM26,20 h3v1H26zM8 21h1v1H8zM10 21h1v1H10zM12 21h1v1H12zM16 21h1v1H16zM18 21h1v1H18zM20 21h1v1H20zM24,21 h5v1H24zM0 22h7v1H0zM10 22h1v1H10zM15 22h2v1H15zM19 22h2v1H19zM22 22h1v1H22zM24 22h3v1H24zM0 23h1v1H0zM6 23h1v1H6zM8 23h1v1H8zM10 23h1v1H10zM14 23h2v1H14zM19 23h2v1H19zM24 23h1v1H24zM27 23h1v1H27zM0 24h1v1H0zM2 24h3v1H2zM6 24h1v1H6zM8 24h5v1H8zM15 24h3v1H15zM20 24h5v1H20zM26,24 h3v1H26zM0 25h1v1H0zM2 25h3v1H2zM6 25h1v1H6zM8 25h1v1H8zM11 25h2v1H11zM14 25h1v1H14zM16 25h1v1H16zM18 25h2v1H18zM21 25h1v1H21zM25,25 h4v1H25zM0 26h1v1H0zM2 26h3v1H2zM6 26h1v1H6zM8 26h3v1H8zM13 26h5v1H13zM21 26h7v1H21zM0 27h1v1H0zM6 27h1v1H6zM9 27h2v1H9zM12 27h5v1H12zM18 27h1v1H18zM20 27h1v1H20zM22 27h1v1H22zM24 27h2v1H24zM27 27h1v1H27zM0 28h7v1H0zM8 28h1v1H8zM10 28h1v1H10zM14 28h1v1H14zM16 28h4v1H16zM22 28h2v1H22zM26 28h1v1H26z"})])],-1))],2)]))}}),U=N(D,[["__scopeId","data-v-f3a34b0a"]]),Y={__name:"slides.md__slidev_55",setup(w){const{$clicksContext:h,$frontmatter:M}=b();return h.setup(),(e,t)=>{const H=U;return _(),R(B,k(P(g(G)(g(M),54))),{default:C(()=>[i(" slide:55 "),T(H)]),_:1},16)}}};export{Y as default};
