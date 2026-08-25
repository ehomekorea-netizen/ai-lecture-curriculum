import{C as e,D as t,F as n,H as r,L as i,S as a,T as o,Z as s,_ as c,b as l,ct as u,g as d,gt as f,v as p,vt as m,y as h,yt as g,z as _}from"./modules/shiki-jL-gh8CJ.js";import{et as v,gt as y,tt as b}from"./index-BUe_D0YT.js";var x={class:`absolute inset-0 w-full h-full flex flex-col justify-between select-none overflow-hidden bg-slate-950 p-12 px-14 text-left font-['Nanum_Gothic',sans-serif]`},S=`
  attribute vec2 position;
  void main() {
    gl_Position = vec4(position, 0.0, 1.0);
  }
`,C=`
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
`,w=y(o({__name:`CoverSlide`,setup(e){let{$slidev:t,$nav:r,$clicksContext:o,$clicks:s,$page:d,$renderContext:f,$frontmatter:p}=b(),m=u(null),g=null,v=null,y=null,w=null,T=null,E=Date.now();function D(e,t,n){let r=e.createShader(t);return r?(e.shaderSource(r,n),e.compileShader(r),e.getShaderParameter(r,e.COMPILE_STATUS)?r:(console.error(`Shader compile error:`,e.getShaderInfoLog(r)),e.deleteShader(r),null)):null}function O(){let e=m.value;if(!e||(v=e.getContext(`webgl`,{antialias:!0,alpha:!1}),!v))return;let t=D(v,v.VERTEX_SHADER,S),n=D(v,v.FRAGMENT_SHADER,C);if(!t||!n||(y=v.createProgram(),!y))return;if(v.attachShader(y,t),v.attachShader(y,n),v.linkProgram(y),!v.getProgramParameter(y,v.LINK_STATUS)){console.error(`Program link error:`,v.getProgramInfoLog(y));return}v.useProgram(y);let r=v.createBuffer();v.bindBuffer(v.ARRAY_BUFFER,r),v.bufferData(v.ARRAY_BUFFER,new Float32Array([-1,-1,1,-1,-1,1,-1,1,1,-1,1,1]),v.STATIC_DRAW);let i=v.getAttribLocation(y,`position`);v.enableVertexAttribArray(i),v.vertexAttribPointer(i,2,v.FLOAT,!1,0,0),w=v.getUniformLocation(y,`u_time`),T=v.getUniformLocation(y,`u_resolution`),k(),A()}function k(){if(!m.value||!v)return;let e=m.value.clientWidth||980,t=m.value.clientHeight||552,n=Math.min(window.devicePixelRatio||1,2);m.value.width=e*n,m.value.height=t*n,v.viewport(0,0,m.value.width,m.value.height)}function A(){if(!v||!y)return;let e=(Date.now()-E)/1e3;w&&v.uniform1f(w,e),T&&m.value&&v.uniform2f(T,m.value.width,m.value.height),v.drawArrays(v.TRIANGLES,0,6),g=requestAnimationFrame(A)}return i(()=>{O(),window.addEventListener(`resize`,k)}),n(()=>{g&&cancelAnimationFrame(g),window.removeEventListener(`resize`,k)}),(e,t)=>(_(),l(`div`,x,[h(` ── Continuous Moving WebGL Fluid Canvas with Silky Smooth Natural Gradient ── `),c(`canvas`,{ref_key:`canvasRef`,ref:m,class:`absolute inset-0 w-full h-full block pointer-events-none`},null,512),h(` ── Top Tag ── `),t[0]||=c(`div`,{class:`relative z-10`},[c(`span`,{class:`inline-block text-xs md:text-sm font-bold tracking-widest text-white uppercase pure-white-text`},` 2026 사회서비스 종사자 디지털 교육 `)],-1),h(` ── Center: Apple Keynote Statement Layout (100% Pure White Floating Title) ── `),t[1]||=c(`div`,{class:`relative z-10 my-auto max-w-3xl space-y-4 pt-2`},[c(`h1`,{class:`text-4xl md:text-[54px] font-extrabold leading-[1.2] tracking-tight pure-white-title`},[a(` AI를 활용한`),c(`br`),a(` 문서 작성 협업 역량 강화 `)]),c(`p`,{class:`text-sm md:text-base font-normal leading-relaxed max-w-xl pure-white-sub`},` 생성형 AI의 작동 원리부터 실무 표준 지시, 도구 협업, 나만의 스킬 자산화까지 `)],-1),h(` ── Bottom Bar: Right-Aligned Presenter Text (오진실 강사) ── `),t[2]||=c(`div`,{class:`relative z-10 flex items-center justify-between border-t border-white/20 pt-4`},[c(`span`,{class:`text-xs text-white/70 font-medium pure-white-text`},` 목포종합사회복지관 `),c(`span`,{class:`text-sm md:text-base font-bold text-white tracking-wide flex items-center gap-2 pure-white-text`},[c(`span`,{class:`text-white/60 font-normal text-xs uppercase tracking-widest`},`Presenter`),a(` 오진실 강사 `)])],-1)]))}}),[[`__scopeId`,`data-v-2b33a4ad`]]);function T(e){return e.startsWith(`/`)?`/mokpo-welfare/`+e.slice(1):e}function E(e,t=!1){let n=e&&[`#`,`rgb`,`hsl`].some(t=>e.indexOf(t)===0),r={background:n?e:void 0,color:e&&!n?`white`:void 0,backgroundImage:n?void 0:e?t?`linear-gradient(#0005, #0008), url(${T(e)})`:`url("${T(e)}")`:void 0,backgroundRepeat:`no-repeat`,backgroundPosition:`center`,backgroundSize:`cover`};return r.background||delete r.background,r}var D={class:`my-auto w-full`},O=o({__name:`cover`,props:{background:{default:``}},setup(e){let{$slidev:t,$nav:n,$clicksContext:i,$clicks:a,$page:o,$renderContext:s,$frontmatter:u}=b(),f=e,p=d(()=>E(f.background,!0));return(e,t)=>(_(),l(`div`,{class:`slidev-layout cover`,style:g(p.value)},[c(`div`,D,[r(e.$slots,`default`)])],4))}}),k={__name:`slides.md__slidev_1`,setup(n){let{$slidev:r,$nav:i,$clicksContext:a,$clicks:o,$page:c,$renderContext:l,$frontmatter:u}=b();return a.setup(),(n,r)=>{let i=w;return _(),p(O,m(t(f(v)(f(u),0))),{default:s(()=>[e(i)]),_:1},16)}}};export{k as default};