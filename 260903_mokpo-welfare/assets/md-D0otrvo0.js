import{C as e,D as t,F as n,L as r,S as i,T as a,Z as o,_ as s,b as c,ct as l,gt as u,v as d,vt as f,y as p,z as m}from"./modules/shiki-jL-gh8CJ.js";import{et as h,gt as g,tt as _}from"./index-A_ZiNcNi.js";import{t as v}from"./slidev/default-BXnC3op3.js";var y={class:`absolute inset-0 w-full h-full flex flex-col justify-center items-center select-none overflow-hidden bg-slate-950 p-10 px-12 text-center font-['Nanum_Gothic',sans-serif]`},b=`
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
`,S=g(a({__name:`EndingSlide`,setup(e){let{$slidev:t,$nav:a,$clicksContext:o,$clicks:u,$page:d,$renderContext:f,$frontmatter:h}=_(),g=l(null),v=null,S=null,C=null,w=null,T=null,E=Date.now();function D(e,t,n){let r=e.createShader(t);return r?(e.shaderSource(r,n),e.compileShader(r),e.getShaderParameter(r,e.COMPILE_STATUS)?r:(console.error(`Shader compile error:`,e.getShaderInfoLog(r)),e.deleteShader(r),null)):null}function O(){let e=g.value;if(!e||(S=e.getContext(`webgl`,{antialias:!0,alpha:!1}),!S))return;let t=D(S,S.VERTEX_SHADER,b),n=D(S,S.FRAGMENT_SHADER,x);if(!t||!n||(C=S.createProgram(),!C))return;if(S.attachShader(C,t),S.attachShader(C,n),S.linkProgram(C),!S.getProgramParameter(C,S.LINK_STATUS)){console.error(`Program link error:`,S.getProgramInfoLog(C));return}S.useProgram(C);let r=S.createBuffer();S.bindBuffer(S.ARRAY_BUFFER,r),S.bufferData(S.ARRAY_BUFFER,new Float32Array([-1,-1,1,-1,-1,1,-1,1,1,-1,1,1]),S.STATIC_DRAW);let i=S.getAttribLocation(C,`position`);S.enableVertexAttribArray(i),S.vertexAttribPointer(i,2,S.FLOAT,!1,0,0),w=S.getUniformLocation(C,`u_time`),T=S.getUniformLocation(C,`u_resolution`),k(),A()}function k(){if(!g.value||!S)return;let e=g.value.clientWidth||980,t=g.value.clientHeight||552,n=Math.min(window.devicePixelRatio||1,2);g.value.width=e*n,g.value.height=t*n,S.viewport(0,0,g.value.width,g.value.height)}function A(){if(!S||!C)return;let e=(Date.now()-E)/1e3;w&&S.uniform1f(w,e),T&&g.value&&S.uniform2f(T,g.value.width,g.value.height),S.drawArrays(S.TRIANGLES,0,6),v=requestAnimationFrame(A)}return r(()=>{O(),window.addEventListener(`resize`,k)}),n(()=>{v&&cancelAnimationFrame(v),window.removeEventListener(`resize`,k)}),(e,t)=>(m(),c(`div`,y,[p(` ── Continuous Moving WebGL Fluid Canvas with Silky Smooth Natural Gradient ── `),s(`canvas`,{ref_key:`canvasRef`,ref:g,class:`absolute inset-0 w-full h-full block pointer-events-none`},null,512),p(` ── Center: Elegant 1.5x Statement Layout ── `),t[0]||=s(`div`,{class:`relative z-10 my-auto w-full max-w-4xl space-y-6 px-4`},[s(`div`,{class:`pure-white-title break-keep`},[i(` AI는 초안을 쓰고,`),s(`br`),i(` 가치는 여러분이 담습니다. `)]),s(`div`,{class:`pure-white-sub`},` 경청해 주셔서 감사합니다. `)],-1)]))}}),[[`__scopeId`,`data-v-5831ce35`]]),C={__name:`slides.md__slidev_40`,setup(n){let{$slidev:r,$nav:i,$clicksContext:a,$clicks:s,$page:c,$renderContext:l,$frontmatter:p}=_();return a.setup(),(n,r)=>{let i=S;return m(),d(v,f(t(u(h)(u(p),39))),{default:o(()=>[e(i)]),_:1},16)}}};export{C as default};