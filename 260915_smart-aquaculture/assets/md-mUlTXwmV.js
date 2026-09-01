import{$ as e,B as t,C as n,D as r,I as i,R as a,S as o,T as s,_ as c,b as l,bt as u,ut as d,v as f,vt as p,y as m}from"./modules/shiki-BoyQGqXc.js";import{ht as h,nt as g,tt as _}from"./index-BhFBpYCJ.js";import{t as v}from"./slidev/default-gY2kG7U5.js";var y={class:`absolute inset-0 w-full h-full flex flex-col justify-between select-none overflow-hidden bg-black p-12 px-14 text-left font-['Pretendard',sans-serif]`},b=`
  attribute vec2 position;
  void main() {
    gl_Position = vec4(position, 0.0, 1.0);
  }
`,x=`
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

    // ── Silky Smooth Natural Gradient (Deep Ocean Navy -> Luminous Sea Teal Glow) ──
    float lightGrad = smoothstep(0.02, 0.95, uv.x);

    vec3 calmNavy = vec3(0.01, 0.04, 0.10);
    vec3 midTeal = vec3(0.04, 0.24, 0.48);
    vec3 brightCyan = vec3(0.12, 0.62, 0.85);
    vec3 peakGlow = vec3(0.38, 0.88, 0.98);

    vec3 col = mix(calmNavy, midTeal, clamp((f * f) * 3.4, 0.0, 1.0));
    col = mix(col, brightCyan, clamp(length(q) * (0.35 + 0.65 * lightGrad), 0.0, 1.0));
    col = mix(col, peakGlow, clamp(length(r.x) * lightGrad * 0.55, 0.0, 1.0));

    // Eye-friendly natural lighting transition
    col = mix(col * 0.72, col * 1.08, lightGrad);

    gl_FragColor = vec4(col, 1.0);
  }
`,S=h(s({__name:`CoverSlide`,setup(e){let{$slidev:n,$nav:r,$clicksContext:s,$clicks:u,$page:f,$renderContext:p,$frontmatter:h}=g(),_=d(null),v=null,S=null,C=null,w=null,T=null,E=Date.now();function D(e,t,n){let r=e.createShader(t);return r?(e.shaderSource(r,n),e.compileShader(r),e.getShaderParameter(r,e.COMPILE_STATUS)?r:(console.error(`Shader compile error:`,e.getShaderInfoLog(r)),e.deleteShader(r),null)):null}function O(){let e=_.value;if(!e||(S=e.getContext(`webgl`,{antialias:!0,alpha:!1}),!S))return;let t=D(S,S.VERTEX_SHADER,b),n=D(S,S.FRAGMENT_SHADER,x);if(!t||!n||(C=S.createProgram(),!C))return;if(S.attachShader(C,t),S.attachShader(C,n),S.linkProgram(C),!S.getProgramParameter(C,S.LINK_STATUS)){console.error(`Program link error:`,S.getProgramInfoLog(C));return}S.useProgram(C);let r=S.createBuffer();S.bindBuffer(S.ARRAY_BUFFER,r),S.bufferData(S.ARRAY_BUFFER,new Float32Array([-1,-1,1,-1,-1,1,-1,1,1,-1,1,1]),S.STATIC_DRAW);let i=S.getAttribLocation(C,`position`);S.enableVertexAttribArray(i),S.vertexAttribPointer(i,2,S.FLOAT,!1,0,0),w=S.getUniformLocation(C,`u_time`),T=S.getUniformLocation(C,`u_resolution`),k(),A()}function k(){if(!_.value||!S)return;let e=_.value.clientWidth||980,t=_.value.clientHeight||552,n=Math.min(window.devicePixelRatio||1,2);_.value.width=e*n,_.value.height=t*n,S.viewport(0,0,_.value.width,_.value.height)}function A(){if(!S||!C)return;let e=(Date.now()-E)/1e3;w&&S.uniform1f(w,e),T&&_.value&&S.uniform2f(T,_.value.width,_.value.height),S.drawArrays(S.TRIANGLES,0,6),v=requestAnimationFrame(A)}return a(()=>{O(),window.addEventListener(`resize`,k)}),i(()=>{v&&cancelAnimationFrame(v),window.removeEventListener(`resize`,k)}),(e,n)=>(t(),l(`div`,y,[m(` ── Continuous Moving WebGL Fluid Canvas with Silky Smooth Natural Gradient ── `),c(`canvas`,{ref_key:`canvasRef`,ref:_,class:`absolute inset-0 w-full h-full block pointer-events-none`},null,512),m(` ── Top Tag ── `),n[0]||=c(`div`,{class:`relative z-10`},[c(`span`,{class:`inline-block text-xs md:text-sm font-bold tracking-widest text-white uppercase pure-white-text`},` 2026년 스마트 수산업 전문인력 양성과정 `)],-1),m(` ── Center: Apple Keynote Statement Layout (100% Pure White Floating Title) ── `),n[1]||=c(`div`,{class:`relative z-10 my-auto max-w-3xl space-y-4 pt-2`},[c(`h1`,{class:`text-4xl md:text-[54px] font-extrabold leading-[1.2] tracking-tight pure-white-title`},[o(` 수산양식과`),c(`br`),o(` 인공지능(AI) 실무 활용 전략 `)]),c(`p`,{class:`text-sm md:text-base font-normal leading-relaxed max-w-xl pure-white-sub`},` 스마트양식 빅데이터부터 머신러닝·딥러닝, 생성형 AI(RCTF), AI 에이전트 운영지원까지 `)],-1),m(` ── Bottom Bar: Right-Aligned Presenter Text (오진실 강사) ── `),n[2]||=c(`div`,{class:`relative z-10 flex items-center justify-end border-t border-white/20 pt-4`},[c(`span`,{class:`text-sm md:text-base font-bold text-white tracking-wide flex items-center gap-2 pure-white-text`},[c(`span`,{class:`text-white/60 font-normal text-xs uppercase tracking-widest`},`Presenter`),o(` 오진실 강사 `)])],-1)]))}}),[[`__scopeId`,`data-v-51602bef`]]),C={__name:`slides.md__slidev_1`,setup(i){let{$slidev:a,$nav:o,$clicksContext:s,$clicks:c,$page:l,$renderContext:d,$frontmatter:h}=g();return s.setup(),(i,a)=>{let o=S;return t(),f(v,u(r(p(_)(p(h),0))),{default:e(()=>[m(` slide:01-Cover `),n(o)]),_:1},16)}}};export{C as default};