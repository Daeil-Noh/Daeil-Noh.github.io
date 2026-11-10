/* 배경: 얽힌 큐비트처럼 연결되는 점들 */
(function(){
  const c=document.getElementById('qbits'); if(!c) return;
  const x=c.getContext('2d'); let w,h,pts;
  const reduce=window.matchMedia('(prefers-reduced-motion: reduce)').matches;
  function init(){
    const r=window.devicePixelRatio||1;
    w=c.offsetWidth; h=c.offsetHeight; c.width=w*r; c.height=h*r; x.setTransform(r,0,0,r,0,0);
    const n=Math.min(70,Math.floor(w*h/14000));
    pts=Array.from({length:n},()=>({x:Math.random()*w,y:Math.random()*h,vx:(Math.random()-.5)*.3,vy:(Math.random()-.5)*.3,p:Math.random()*6.28}));
  }
  function draw(){
    x.clearRect(0,0,w,h);
    for(const a of pts){a.x+=a.vx;a.y+=a.vy;a.p+=.02;if(a.x<0||a.x>w)a.vx*=-1;if(a.y<0||a.y>h)a.vy*=-1;}
    for(let i=0;i<pts.length;i++)for(let j=i+1;j<pts.length;j++){
      const a=pts[i],b=pts[j],d=Math.hypot(a.x-b.x,a.y-b.y);
      if(d<130){x.strokeStyle='rgba(140,160,255,'+(1-d/130)*.5+')';x.lineWidth=1;x.beginPath();x.moveTo(a.x,a.y);x.lineTo(b.x,b.y);x.stroke();}
    }
    for(const a of pts){x.fillStyle='rgba(190,175,255,'+(.55+.45*Math.sin(a.p))+')';x.beginPath();x.arc(a.x,a.y,2,0,6.28);x.fill();}
    if(!reduce) requestAnimationFrame(draw);
  }
  init(); draw(); addEventListener('resize',()=>{init(); if(reduce) draw();});
})();
