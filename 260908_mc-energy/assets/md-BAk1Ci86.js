import{E as e,I as t,P as n,R as r,S as i,Z as a,_ as o,b as s,ct as c,g as l,gt as u,v as d,vt as f,w as p,y as m}from"./modules/shiki-DSMc7FDf.js";import{et as h,gt as g,tt as _}from"./index-DTRx2rdP.js";import{t as v}from"./slidev/default-Ozos5JVv.js";var y={class:`absolute inset-0 w-full h-full flex flex-col justify-between select-none overflow-hidden bg-black p-12 px-14 text-left font-['Pretendard',sans-serif]`},b=`
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

    // ── Silky Smooth MC Energy Gradient (Deep Navy -> Cobalt Blue -> Electric Cyan Glow) ──
    float lightGrad = smoothstep(0.02, 0.95, uv.x);

    vec3 calmNavy = vec3(0.01, 0.03, 0.12);
    vec3 midBlue = vec3(0.00, 0.20, 0.65);
    vec3 brightCyan = vec3(0.08, 0.55, 0.88);
    vec3 peakGlow = vec3(0.35, 0.85, 0.98);

    vec3 col = mix(calmNavy, midBlue, clamp((f * f) * 3.4, 0.0, 1.0));
    col = mix(col, brightCyan, clamp(length(q) * (0.35 + 0.65 * lightGrad), 0.0, 1.0));
    col = mix(col, peakGlow, clamp(length(r.x) * lightGrad * 0.55, 0.0, 1.0));

    // Eye-friendly natural lighting transition
    col = mix(col * 0.72, col * 1.08, lightGrad);

    gl_FragColor = vec4(col, 1.0);
  }
`,S=g(p({__name:`CoverSlide`,setup(e){let{$slidev:i,$nav:a,$clicksContext:o,$clicks:u,$page:f,$renderContext:p,$frontmatter:h}=_(),g=c(null),v=null,S=null,C=null,w=null,T=null,E=Date.now();function D(e,t,n){let r=e.createShader(t);return r?(e.shaderSource(r,n),e.compileShader(r),e.getShaderParameter(r,e.COMPILE_STATUS)?r:(console.error(`Shader compile error:`,e.getShaderInfoLog(r)),e.deleteShader(r),null)):null}function O(){let e=g.value;if(!e||(S=e.getContext(`webgl`,{antialias:!0,alpha:!1}),!S))return;let t=D(S,S.VERTEX_SHADER,b),n=D(S,S.FRAGMENT_SHADER,x);if(!t||!n||(C=S.createProgram(),!C))return;if(S.attachShader(C,t),S.attachShader(C,n),S.linkProgram(C),!S.getProgramParameter(C,S.LINK_STATUS)){console.error(`Program link error:`,S.getProgramInfoLog(C));return}S.useProgram(C);let r=S.createBuffer();S.bindBuffer(S.ARRAY_BUFFER,r),S.bufferData(S.ARRAY_BUFFER,new Float32Array([-1,-1,1,-1,-1,1,-1,1,1,-1,1,1]),S.STATIC_DRAW);let i=S.getAttribLocation(C,`position`);S.enableVertexAttribArray(i),S.vertexAttribPointer(i,2,S.FLOAT,!1,0,0),w=S.getUniformLocation(C,`u_time`),T=S.getUniformLocation(C,`u_resolution`),k(),A()}function k(){if(!g.value||!S)return;let e=g.value.clientWidth||980,t=g.value.clientHeight||552,n=Math.min(window.devicePixelRatio||1,2);g.value.width=e*n,g.value.height=t*n,S.viewport(0,0,g.value.width,g.value.height)}function A(){if(!S||!C)return;let e=(Date.now()-E)/1e3;w&&S.uniform1f(w,e),T&&g.value&&S.uniform2f(T,g.value.width,g.value.height),S.drawArrays(S.TRIANGLES,0,6),v=requestAnimationFrame(A)}return t(()=>{O(),window.addEventListener(`resize`,k)}),n(()=>{v&&cancelAnimationFrame(v),window.removeEventListener(`resize`,k)}),(e,t)=>(r(),m(`div`,y,[d(` ── Continuous Moving WebGL Fluid Canvas with Silky Smooth Natural Gradient ── `),l(`canvas`,{ref_key:`canvasRef`,ref:g,class:`absolute inset-0 w-full h-full block pointer-events-none`},null,512),d(` ── Top Tag ── `),t[0]||=l(`div`,{class:`relative z-10`},[l(`span`,{class:`inline-block text-xs md:text-sm font-bold tracking-widest text-white uppercase pure-white-text`},` 2026년 MC에너지 AI 실무역량 강화과정 `)],-1),d(` ── Center: Apple Keynote Statement Layout (100% Pure White Floating Title) ── `),t[1]||=l(`div`,{class:`relative z-10 my-auto max-w-4xl space-y-4 pt-2`},[l(`h1`,{class:`text-3xl md:text-[46px] font-extrabold leading-[1.2] tracking-tight pure-white-title whitespace-nowrap`},` 생성형 AI를 통한 실무능력 향상 `),l(`p`,{class:`text-sm md:text-base font-normal leading-relaxed max-w-2xl pure-white-sub`},` AI의 본질과 2026 트렌드부터 개인 맞춤설정, 보안 마스킹, 그리고 안전한 RCTF 지시법까지 `)],-1),d(` ── Bottom Bar: Logos & Presenter Text ── `),t[2]||=s(`<div class="relative z-10 flex items-center justify-between border-t border-white/20 pt-4" data-v-735762d6><div class="flex items-center gap-2.5" data-v-735762d6><img src="/260908_mc-energy/mc-energy-logo.jpg" alt="MC Energy" class="h-6.5 rounded px-2.5 py-1 bg-white object-contain shadow-sm" data-v-735762d6><img src="/260908_mc-energy/smhrd-logo.png" alt="스마트인재개발원" class="h-6.5 rounded px-2.5 py-1 bg-white object-contain shadow-sm" data-v-735762d6></div><span class="text-sm md:text-base font-bold text-white tracking-wide flex items-center gap-2 pure-white-text" data-v-735762d6><span class="text-white/60 font-normal text-xs uppercase tracking-widest" data-v-735762d6>Presenter</span> 오진실 강사 </span></div>`,1)]))}}),[[`__scopeId`,`data-v-735762d6`]]),C={__name:`slides.md__slidev_1`,setup(t){let{$slidev:n,$nav:s,$clicksContext:c,$clicks:l,$page:p,$renderContext:m,$frontmatter:g}=_();return c.setup(),(t,n)=>{let s=S;return r(),o(v,f(e(u(h)(u(g),0))),{default:a(()=>[d(` slide:01-Cover `),i(s)]),_:1},16)}}};export{C as default};