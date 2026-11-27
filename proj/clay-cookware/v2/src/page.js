(function () {
  'use strict';
  var $ = function (s, r) {
    return (r || document).querySelector(s);
  };
  var $$ = function (s, r) {
    return Array.prototype.slice.call((r || document).querySelectorAll(s));
  };
  var NS = 'http://www.w3.org/2000/svg';
  var reduce = window.matchMedia && window.matchMedia('(prefers-reduced-motion: reduce)').matches;
  function c() {
    var ns = Array.prototype.slice.call(arguments);
    return (
      '<sup class="fn">' +
      ns
        .map(function (n) {
          return '<a href="#s' + n + '" aria-label="source ' + n + '">' + n + '</a>';
        })
        .join(',') +
      '</sup>'
    );
  }
  function el(tag, attrs, parent) {
    var e = document.createElementNS(NS, tag);
    for (var k in attrs) e.setAttribute(k, attrs[k]);
    if (parent) parent.appendChild(e);
    return e;
  }
  function press(btns, on) {
    btns.forEach(function (b) {
      b.setAttribute('aria-pressed', b === on ? 'true' : 'false');
    });
  }
  function fToC(f) {
    return Math.round(((f - 32) * 5) / 9);
  }
  function fmt(n) {
    return n.toLocaleString('en-US');
  }

  /* ================= the pot picker (running device) ================= */
  var POTS = {
    rt: 'Römertopf',
    lc: 'La Chamba',
    vc: 'VitaClay',
    mg: 'Magnifique',
    al: 'Aluminum insert',
    ci: 'Cast-iron insert',
  };
  var current = 'rt';
  try {
    var saved = localStorage.getItem('clay-v2-pot');
    if (saved && POTS[saved]) current = saved;
  } catch (e) {}

  function setPot(id, focusFamily) {
    current = id;
    try {
      localStorage.setItem('clay-v2-pot', id);
    } catch (e) {}
    $$('[data-pot]', $('#heropots')).forEach(function (b) {
      b.setAttribute('aria-pressed', b.dataset.pot === id ? 'true' : 'false');
    });
    $$('[data-pot]', $('#pickbtns')).forEach(function (b) {
      b.setAttribute('aria-pressed', b.dataset.pot === id ? 'true' : 'false');
    });
    $('#pickname').textContent = POTS[id];
    $$('.verdicts').forEach(function (v) {
      var mine = null;
      $$('.v-list li', v).forEach(function (li) {
        var on = li.dataset.pot === id;
        li.classList.toggle('mine', on);
        if (on) mine = li;
      });
      var box = $('.v-mine', v);
      if (mine && box) {
        var txt = mine.innerHTML.replace(/^<svg[\s\S]*?<\/svg>/, '').replace(/^<b>[^<]*<\/b>/, '');
        box.innerHTML =
          '<svg aria-hidden="true"><use href="#i-' +
          id +
          '"/></svg><div><div class="who">Your pot · ' +
          POTS[id] +
          '</div><div class="what">' +
          txt +
          '</div></div>';
      }
    });
    $$('#matrix [data-pot]').forEach(function (cell) {
      cell.classList.toggle('mine', cell.dataset.pot === id);
    });
    renderStove();
    if (focusFamily !== false) selectFamily(POT_FAMILY[id] || 'terra');
  }
  $$('.v-list li').forEach(function (li) {
    li.insertAdjacentHTML('afterbegin', '<svg aria-hidden="true"><use href="#i-' + li.dataset.pot + '"/></svg>');
  });
  $$('#heropots [data-pot], #pickbtns [data-pot]').forEach(function (b) {
    b.addEventListener('click', function () {
      setPot(b.dataset.pot);
    });
  });

  /* ================= progress rail ================= */
  var chapters = $$('section[data-name]');
  var dots = $$('#raildots a');
  function onScroll() {
    var y = window.scrollY,
      h = document.documentElement.scrollHeight - window.innerHeight;
    $('#railbar').style.width = (h > 0 ? Math.min(100, (y / h) * 100) : 0) + '%';
    var now = null;
    chapters.forEach(function (s) {
      if (s.getBoundingClientRect().top < window.innerHeight * 0.35) now = s;
    });
    $('#railnow').textContent = now ? "It's All in the Wall · " + now.dataset.name : "It's All in the Wall";
    dots.forEach(function (d) {
      d.classList.toggle('on', !!now && d.getAttribute('href') === '#' + now.id);
    });
  }
  window.addEventListener('scroll', onScroll, { passive: true });

  /* ================= generic range bars ================= */
  // row: {name, sub, lo, hi, color, val, gap, single}
  function renderBars(host, rows, max) {
    host.innerHTML = '';
    rows.forEach(function (r) {
      var row = document.createElement('div');
      row.className = 'bar' + (r.gap ? ' bar-gap' : '');
      var label =
        '<div class="bar-name">' +
        r.name +
        (r.sub ? '<small>' + r.sub + '</small>' : '') +
        '<small><b style="color:inherit">' +
        r.val +
        '</b></small></div>';
      var track =
        '<div class="bar-track" role="img" aria-label="' +
        (r.aria || r.name.replace(/<[^>]+>/g, '') + ': ' + r.val.replace(/<[^>]+>/g, '')) +
        '">';
      if (r.gap) {
        track += '<span class="bar-val">' + (r.gapText || 'not measured') + '</span>';
      } else {
        var lo = (Math.min(r.lo, max) / max) * 100,
          hi = (Math.min(r.hi, max) / max) * 100;
        if (r.single && lo < 0.6) lo = 0.6;
        track += '<span class="bar-fill" style="width:' + lo + '%;background:' + r.color + '"></span>';
        if (hi > lo)
          track +=
            '<span class="bar-span" style="left:' +
            lo +
            '%;width:' +
            (hi - lo) +
            '%;background-color:' +
            r.color +
            '"></span>';
        if (r.hi > max) track += '<span class="bar-off">off scale →</span>';
      }
      track += '</div>';
      row.innerHTML = label + track;
      host.appendChild(row);
    });
  }
  function ticks(host, max, unit) {
    var out = '';
    for (var i = 0; i <= 4; i++) {
      var v = (max * i) / 4;
      var s = v >= 100 ? fmt(Math.round(v)) : (Math.round(v * 100) / 100).toString();
      out += '<span>' + s + (i === 4 ? ' ' + unit : '') + '</span>';
    }
    host.innerHTML = out;
  }

  /* ================= plate 1: the wall ================= */
  var WALLS = [
    { id: 'tc', name: 'Unglazed terracotta', sub: 'Römertopf · fired 900–1,063°C', fill: '#C2603F' },
    { id: 'zs', name: 'Unglazed Zisha', sub: 'VitaClay · fired 1,100–1,220°C', fill: '#7A4038' },
    { id: 'ch', name: 'Burnished micaceous clay', sub: 'La Chamba · fired 750–800°C', fill: '#2A2623' },
    { id: 'gl', name: 'Glazed kaolin stoneware', sub: 'Magnifique · glass face', fill: '#BDB3A6' },
  ];
  var WALLTEXT = {
    water: {
      say: {
        tc: ['Drinks it', '8–25% of its weight'],
        zs: ['Barely', 'about 2–6%; no soak'],
        ch: ['Slowly', 'burnished skin slows it'],
        gl: ['Sheds it', 'about 0% through glaze'],
      },
      read:
        '<b>Cold-water soak.</b> Terracotta’s open pores fill in 10–20 minutes, which is what lets a cold oven turn the pot into a steam chamber near 212°F; Zisha takes up only about 2–6%, and VitaClay says never to soak its outside; La Chamba’s burnished skin slows water down; and glaze lets none of it through.' +
        c(2, 14, 17, 11),
    },
    oil: {
      say: {
        tc: ['Deep', 'fats go 5–400+ µm in'],
        zs: ['Into the pores', 'fats and aromas stay'],
        ch: ['Builds up', 'over repeated use'],
        gl: ['Wipes off', 'no flavor memory'],
      },
      read:
        '<b>Cooking oil and aromas.</b> Fats, not broth, are what get in: fatty acids such as palmitic and stearic acid travel 5–400+ µm into an unglazed wall, and since clay can’t be baked hot enough to polymerize them the way cast-iron seasoning does, unsaturated oils can turn rancid between uses; a glaze keeps all of it on the surface.' +
        c(27, 26, 6),
    },
    soap: {
      say: {
        tc: ['Soaks in', 'use salt or baking soda'],
        zs: ['Mild soap only', 'rinse thoroughly'],
        ch: ['Go easy', 'warm water, no detergent'],
        gl: ['No problem', 'dishwasher-safe'],
      },
      read:
        '<b>Dish soap.</b> Soap surfactants are pulled into unglazed pores and cling to the clay minerals, then leach back out as a soapy taste on reheating; newer Römertopf and VitaClay manuals allow a little mild soap with a thorough hot rinse, and glaze doesn’t care at all.' +
        c(26, 17, 14),
    },
    flame: {
      say: {
        tc: ['Cracks', 'oven only'],
        zs: ['Banned', 'electric base only'],
        ch: ['Survives, low–medium', 'mica stops the crack'],
        gl: ['Rated', 'gradual stovetop heat'],
      },
      read:
        '<b>Gas flame.</b> Clay moves heat so slowly (0.5–4.0 W/(m·K)) that a flame’s heat pools where it touches: plain terracotta and ordinary Zisha crack; La Chamba’s mica and open pores stop small cracks before they spread; and Magnifique’s glazed body is rated for gradual stovetop heat.' +
        c(12, 20, 17, 7),
    },
  };
  // deterministic pseudo-random pore fields
  function rng(seed) {
    return function () {
      seed = (seed * 9301 + 49297) % 233280;
      return seed / 233280;
    };
  }
  var PORES = {};
  (function () {
    var r = rng(7),
      a = [];
    for (var i = 0; i < 15; i++) a.push([24 + i * 38 + r() * 10, 40 + r() * 46, 5 + r() * 3.5]);
    PORES.tc = a;
    r = rng(11);
    a = [];
    for (i = 0; i < 46; i++) a.push([10 + i * 12.6 + r() * 4, 34 + r() * 56, 1.6 + r() * 1.2]);
    PORES.zs = a;
    r = rng(5);
    a = [];
    for (i = 0; i < 12; i++) a.push([30 + i * 46 + r() * 12, 42 + r() * 44, 2.6 + r() * 1.4]);
    PORES.ch = a;
    r = rng(3);
    a = [];
    for (i = 0; i < 10; i++) a.push([40 + i * 56 + r() * 10, 50 + r() * 36, 1.4]);
    PORES.gl = a;
  })();

  function drawWall(svg, w) {
    svg.innerHTML = '';
    el('rect', { x: 0, y: 0, width: 600, height: 124, fill: '#FFFCF6' }, svg);
    el('text', { x: 6, y: 13, 'font-size': 10.5, fill: '#4E463E', 'font-weight': 600 }, svg).textContent = 'food side';
    el('text', { x: 6, y: 120, 'font-size': 10.5, fill: '#4E463E', 'font-weight': 600 }, svg).textContent = 'outside';
    var top = w.id === 'gl' ? 34 : 26;
    el('rect', { x: 0, y: 26, width: 600, height: 72, fill: w.fill }, svg);
    if (w.id === 'gl') {
      el('rect', { x: 0, y: 26, width: 600, height: 8, fill: '#1B5674' }, svg);
      el('path', { d: 'M20 29 H120 M200 29 H330 M420 29 H520', stroke: '#BFE0EE', 'stroke-width': 1.5 }, svg);
    }
    if (w.id === 'ch') {
      el('rect', { x: 0, y: 26, width: 600, height: 3, fill: '#A49B8E' }, svg);
      var r = rng(9);
      for (var i = 0; i < 16; i++) {
        var x = 14 + i * 37 + r() * 8,
          y = 40 + r() * 50,
          ang = (r() - 0.5) * 18;
        el(
          'rect',
          {
            x: x,
            y: y,
            width: 18 + r() * 8,
            height: 2.6,
            fill: '#D9D1C4',
            transform: 'rotate(' + ang.toFixed(1) + ' ' + x + ' ' + y + ')',
          },
          svg
        );
      }
    }
    if (w.id === 'tc') {
      PORES.tc.forEach(function (p, i) {
        if (i % 2 === 0)
          el('path', { d: 'M' + p[0] + ' 26 L' + (p[0] + 4) + ' ' + p[1], stroke: '#F3E6DB', 'stroke-width': 3 }, svg);
      });
    }
    var pg = el('g', { class: 'pores' }, svg);
    PORES[w.id].forEach(function (p) {
      el(
        'circle',
        {
          cx: p[0].toFixed(1),
          cy: Math.max(top + 4, p[1]).toFixed(1),
          r: p[2].toFixed(1),
          fill: w.id === 'ch' ? '#4A433D' : w.id === 'gl' ? '#A99F92' : '#F3E6DB',
        },
        pg
      );
    });
    el('g', { class: 'fx' }, svg);
  }

  function wallFx(svg, w, mode) {
    var g = svg.querySelector('.fx');
    g.innerHTML = '';
    var pores = PORES[w.id];
    var blue = '#2B6F96',
      amber = '#C98A16',
      soap = '#6B4C8A';
    var anim = !reduce;
    function drop(x, yEnd, color, delay, rx) {
      var e = el('ellipse', { cx: x, cy: yEnd, rx: rx || 3.2, ry: 4.2, fill: color }, g);
      if (anim) {
        e.setAttribute('class', 'fx-drop');
        e.style.animationDelay = delay + 's';
      }
      return e;
    }
    function later(node, delay, cls) {
      if (anim) {
        node.setAttribute('class', cls || 'fx-fill');
        node.style.animationDelay = delay + 's';
      }
      return node;
    }
    var i, p;
    if (mode === 'water' || mode === 'soap') {
      var col = mode === 'water' ? blue : soap;
      if (w.id === 'tc') {
        for (i = 0; i < pores.length; i += 1) {
          p = pores[i];
          if (mode === 'water') drop(p[0], 20, col, i * 0.05);
          later(
            el(
              'circle',
              mode === 'water'
                ? { cx: p[0], cy: p[1], r: p[2] - 0.6, fill: col }
                : { cx: p[0], cy: p[1], r: p[2] - 1.5, fill: 'none', stroke: col, 'stroke-width': 1.8 },
              g
            ),
            0.8 + i * 0.05
          );
        }
      } else if (w.id === 'zs') {
        later(el('rect', { x: 0, y: 21, width: 600, height: 5, fill: col, opacity: 0.85 }, g), 0.6);
        for (i = 0; i < pores.length; i++) {
          p = pores[i];
          if (i % 4 === 0) drop(p[0], 18, col, i * 0.02);
          if (p[1] < 50) later(el('circle', { cx: p[0], cy: p[1], r: p[2], fill: col }, g), 1 + i * 0.02);
        }
      } else if (w.id === 'ch') {
        later(el('rect', { x: 0, y: 21, width: 600, height: 5, fill: col, opacity: 0.85 }, g), 0.6);
        for (i = 0; i < pores.length; i++) {
          p = pores[i];
          drop(p[0], 18, col, i * 0.04);
          if (p[1] < 56) later(el('circle', { cx: p[0], cy: p[1], r: p[2] - 0.4, fill: col }, g), 1.6 + i * 0.05);
        }
      } else {
        for (i = 0; i < 14; i++) {
          var x = 22 + i * 42;
          if (mode === 'water') drop(x, 21, col, i * 0.04, 6);
          else
            later(
              el('circle', { cx: x, cy: 17, r: 4.5, fill: 'none', stroke: col, 'stroke-width': 1.6 }, g),
              0.3 + i * 0.04
            );
        }
      }
      if (mode === 'soap' && w.id !== 'gl') {
        for (i = 0; i < 10; i++)
          later(
            el('circle', { cx: 30 + i * 60, cy: 16, r: 4.5, fill: 'none', stroke: col, 'stroke-width': 1.6 }, g),
            i * 0.04,
            'fx-drop'
          );
      }
    } else if (mode === 'oil') {
      var depth = { tc: 90, zs: 58, ch: 48, gl: 0 }[w.id];
      later(el('rect', { x: 0, y: 21, width: 600, height: 5, fill: amber }, g), 0);
      if (depth) {
        for (i = 0; i < 24; i++) {
          var ox = 12 + i * 25;
          var d = 26 + (depth - 26) * (0.55 + 0.45 * Math.abs(Math.sin(i * 1.7)));
          var ln = el(
            'path',
            {
              d: 'M' + ox + ' 26 L' + (ox + 3) + ' ' + d.toFixed(1),
              stroke: amber,
              'stroke-width': 2.4,
              'stroke-linecap': 'round',
              fill: 'none',
            },
            g
          );
          if (anim) {
            ln.setAttribute('class', 'fx-draw');
            ln.style.animationDelay = 0.3 + i * 0.03 + 's';
          }
        }
      }
    } else if (mode === 'flame') {
      for (i = 0; i < 9; i++) {
        var fx = 150 + i * 34,
          fh = 14 + (i % 3) * 5;
        var f = el(
          'path',
          {
            d:
              'M' +
              (fx - 7) +
              ' 124 Q' +
              (fx - 8) +
              ' ' +
              (124 - fh * 0.6) +
              ' ' +
              fx +
              ' ' +
              (124 - fh) +
              ' Q' +
              (fx + 8) +
              ' ' +
              (124 - fh * 0.6) +
              ' ' +
              (fx + 7) +
              ' 124 Z',
            fill: i % 2 ? '#F2A65A' : '#2F7FC1',
          },
          g
        );
        if (anim) {
          f.setAttribute('class', 'fx-flame');
          f.style.animationDelay = i * 0.07 + 's';
        }
      }
      var crack = null;
      if (w.id === 'tc') crack = 'M300 98 L292 84 L306 72 L296 58 L310 46 L300 34 L306 26';
      if (w.id === 'zs') crack = 'M290 98 L298 82 L286 70 L300 56 L292 42 L302 26';
      if (w.id === 'ch') crack = 'M300 98 L294 86 L306 78 L318 76';
      if (crack) {
        var cp = el(
          'path',
          {
            d: crack,
            stroke: w.id === 'ch' ? '#F2A65A' : '#FFFFFF',
            'stroke-width': 2.6,
            fill: 'none',
            'stroke-linejoin': 'round',
          },
          g
        );
        var cp2 = el('path', { d: crack, stroke: '#1C1916', 'stroke-width': 1, fill: 'none' }, g);
        if (anim) {
          [cp, cp2].forEach(function (n) {
            n.setAttribute('class', 'fx-draw');
            n.style.animationDelay = '0.5s';
          });
        }
        if (w.id === 'ch') {
          var stop = el('circle', { cx: 318, cy: 76, r: 5, fill: 'none', stroke: '#F2A65A', 'stroke-width': 2 }, g);
          later(stop, 1.4);
        }
      } else {
        later(el('path', { d: 'M286 108 l8 8 l16 -16', stroke: '#1F6040', 'stroke-width': 3, fill: 'none' }, g), 0.4);
      }
    }
  }

  var wallMode = 'water';
  var wallsHost = $('#walls');
  WALLS.forEach(function (w) {
    var row = document.createElement('div');
    row.className = 'wall';
    row.innerHTML =
      '<div class="wall-name"><b>' +
      w.name +
      '</b><small>' +
      w.sub +
      '</small></div><svg viewBox="0 0 600 124" role="img" aria-label="Cross-section of ' +
      w.name +
      ' wall"></svg><div class="wall-say" id="say-' +
      w.id +
      '"></div>';
    wallsHost.appendChild(row);
    w.svg = $('svg', row);
    drawWall(w.svg, w);
  });
  function renderWall() {
    var t = WALLTEXT[wallMode];
    WALLS.forEach(function (w) {
      wallFx(w.svg, w, wallMode);
      var s = t.say[w.id];
      var say = $('#say-' + w.id);
      say.innerHTML = s[0] + '<small>' + s[1] + '</small>';
      w.svg.setAttribute('aria-label', w.name + ' wall, ' + wallMode + ' test: ' + s[0] + ', ' + s[1]);
    });
    $('#wallread').innerHTML = t.read;
  }
  var wallBtns = $$('[data-wall]');
  wallBtns.forEach(function (b) {
    b.addEventListener('click', function () {
      wallMode = b.dataset.wall;
      press(wallBtns, b);
      renderWall();
    });
  });
  (function () {
    var rows = '';
    WALLS.forEach(function (w) {
      rows += '<tr><td><b>' + w.name + '</b><br>' + w.sub + '</td>';
      ['water', 'oil', 'soap', 'flame'].forEach(function (m) {
        var s = WALLTEXT[m].say[w.id];
        rows += '<td>' + s[0] + ': ' + s[1] + '</td>';
      });
      rows += '</tr>';
    });
    $('#walltable').innerHTML = rows;
  })();

  renderBars(
    $('#absbars'),
    [
      {
        name: 'Unglazed terracotta',
        sub: 'Römertopf',
        lo: 8,
        hi: 25,
        color: '#B8532F',
        val: '8–25% (full span about 4–25%+)',
      },
      {
        name: 'Unglazed Zisha',
        sub: 'VitaClay; China’s standard caps it at 6%',
        lo: 2,
        hi: 6,
        color: '#6E3B36',
        val: 'about 2–6%',
      },
      {
        name: 'Vitreous stoneware body',
        sub: 'the clay under a glaze',
        lo: 0.5,
        hi: 3,
        color: '#1B5674',
        val: '0.5–3%',
      },
      { name: 'Porcelain', sub: '', lo: 0, hi: 0.5, color: '#1B5674', val: '0.5% or less' },
      {
        name: 'A glazed surface',
        sub: 'the glass layer itself',
        lo: 0,
        hi: 0,
        color: '#1B5674',
        val: 'about 0%',
        single: true,
      },
      {
        name: 'La Chamba',
        sub: 'low-fired, burnished',
        gap: true,
        val: 'never lab-measured',
        gapText: 'never measured in a lab; low-fired micaceous sherds show 21–26% porosity, a different measure',
      },
    ],
    25
  );

  /* ================= plate 2: the clay families ================= */
  var FAMS = [
    {
      id: 'chamba',
      name: 'Burnished micaceous',
      sub: 'La Chamba; New Mexico Pueblo pots',
      main: [750, 800],
      broad: [600, 900],
      color: '#26221F',
      fired: '750–800°C (broadly 600–900°C)' + c(5),
      water: 'Never lab-measured; low-fired micaceous sherds measure 21–26% porosity' + c(6),
      heat:
        'Flat mica flakes (stable below 900°C) and sandy grit deflect small cracks, so it survives a gentle flame' +
        c(20),
      ex: 'La Chamba (Colombia), Northern New Mexico Pueblo pots',
    },
    {
      id: 'terra',
      name: 'Red earthenware',
      sub: 'terracotta; Römertopf',
      main: [900, 1063],
      broad: [800, 1063],
      color: '#B8532F',
      fired: '900–1,063°C (tagines about 800–1,000°C)' + c(1),
      water: '8–25% (full span about 4–25%+)' + c(2),
      heat: 'High thermal expansion (4.5–8.0 millionths per °C); cracks on burners unless heavily tempered' + c(23),
      ex: 'Römertopf, unglazed Moroccan tagines, Spanish <em>cazuelas</em>',
    },
    {
      id: 'volc',
      name: '“Volcanic clay”',
      sub: "Korean <tspan font-style='italic'>onggi</tspan>, <tspan font-style='italic'>ttukbaegi</tspan>",
      subHtml: 'Korean <em>onggi</em>, <em>ttukbaegi</em>',
      main: [900, 1250],
      more: true,
      color: '#7B6A5A',
      fired: '900–1,250°C and up' + c(9),
      water:
        'Traditional <em>onggi</em>: 10.8–38.2% porosity; modern petalite <em>ttukbaegi</em>: near 0% absorption' +
        c(9),
      heat: 'A marketing label: the crack-proof modern pots get their resistance from added petalite' + c(9),
      ex: 'Korean <em>onggi</em> and <em>ttukbaegi</em>, Jeju scoria-blended wares',
    },
    {
      id: 'zisha',
      name: 'Zisha',
      sub: 'Yixing purple clay; VitaClay',
      main: [1100, 1200],
      broad: [1100, 1220],
      color: '#6E3B36',
      fired: '1,100–1,200°C (VitaClay states 1,100–1,220°C)' + c(3, 17),
      water: 'About 2–6%; China’s GB/T 10816 caps it at 6.0%' + c(4),
      heat: 'Quartz, mullite, hematite and glass with two sizes of pores; ordinary teaware cracks on a flame' + c(3),
      ex: 'VitaClay inserts, Yixing teapots',
    },
    {
      id: 'flame',
      name: 'LAS / MAS flameware',
      sub: 'petalite, spodumene, cordierite',
      main: [1100, 1350],
      color: '#1F6040',
      fired: '1,100–1,350°C' + c(23),
      water: 'Near 0% (Pyroceram) to low' + c(23),
      heat:
        'Lithium or magnesium minerals push expansion to about −0.5 to 3.5 millionths per °C, so it survives a 300–800°C jump' +
        c(23),
      ex: 'Banko-yaki <em>donabe</em> (about 40–50% petalite), CorningWare (Pyroceram 9608)',
    },
    {
      id: 'kaolin',
      name: 'Kaolin stoneware, porcelain',
      sub: 'glazed crocks and bakeware',
      main: [1186, 1400],
      more: true,
      color: '#1B5674',
      fired: '1,186–1,400°C and up' + c(1),
      water: '0.5–3% (stoneware); 0.5% or less (porcelain)' + c(2),
      heat: 'Dense, strong and watertight, but brittle under a burner’s hot spot unless the body is tuned' + c(20),
      ex: 'Slow-cooker crocks, glazed baking dishes; Magnifique is sold as kaolin, fired above 815°C' + c(7),
    },
  ];
  var POT_FAMILY = { rt: 'terra', lc: 'chamba', vc: 'zisha', mg: 'kaolin' };
  var famSel = 'terra';
  var fam = $('#famchart');
  var X0 = 210,
    X1 = 620,
    T0 = 500,
    T1 = 1500;
  function fx(t) {
    return X0 + ((t - T0) / (T1 - T0)) * (X1 - X0);
  }
  (function drawFam() {
    // grid & axis
    for (var t = 500; t <= 1500; t += 250) {
      el('line', { x1: fx(t), x2: fx(t), y1: 14, y2: 336, stroke: '#CBBFAC', 'stroke-width': 1 }, fam);
      var tx = el('text', { x: fx(t), y: 354, 'text-anchor': 'middle', 'font-size': 12, fill: '#4E463E' }, fam);
      tx.textContent = fmt(t) + '°C';
      if (t === 1500) tx.setAttribute('text-anchor', 'end');
    }
    el('line', { x1: X0, x2: X1, y1: 336, y2: 336, stroke: '#1C1916', 'stroke-width': 1.5 }, fam);
    el(
      'line',
      { x1: fx(573), x2: fx(573), y1: 14, y2: 336, stroke: '#A12A1A', 'stroke-width': 1.5, 'stroke-dasharray': '4 4' },
      fam
    );
    var q = el('text', { x: fx(573) + 4, y: 374, 'font-size': 11.5, fill: '#A12A1A', 'font-weight': 600 }, fam);
    q.textContent = '573°C: quartz suddenly expands';
    FAMS.forEach(function (f, i) {
      var y = 22 + i * 52;
      var g = el(
        'g',
        {
          class: 'row',
          tabindex: 0,
          role: 'button',
          'data-fam': f.id,
          'aria-label':
            f.name.replace(/[“”]/g, '') +
            ', fired ' +
            f.main[0] +
            ' to ' +
            f.main[1] +
            '°C' +
            (f.more ? ' and up' : ''),
        },
        fam
      );
      el('rect', { class: 'hit', x: 0, y: y - 6, width: 640, height: 50, fill: 'transparent' }, g);
      var n = el('text', { x: 6, y: y + 14, 'font-size': 14, 'font-weight': 700, fill: '#1C1916' }, g);
      n.textContent = f.name;
      var s = el('text', { x: 6, y: y + 31, 'font-size': 11.5, fill: '#4E463E' }, g);
      s.innerHTML = f.sub;
      if (f.broad)
        el(
          'rect',
          {
            x: fx(f.broad[0]),
            y: y + 8,
            width: fx(f.broad[1]) - fx(f.broad[0]),
            height: 18,
            fill: f.color,
            opacity: 0.28,
          },
          g
        );
      el(
        'rect',
        { x: fx(f.main[0]), y: y + 4, width: Math.max(4, fx(f.main[1]) - fx(f.main[0])), height: 26, fill: f.color },
        g
      );
      if (f.more)
        el(
          'path',
          {
            d: 'M' + (fx(f.main[1]) + 2) + ' ' + (y + 17) + ' h14 m-5 -5 l5 5 l-5 5',
            stroke: f.color,
            'stroke-width': 2.2,
            fill: 'none',
          },
          g
        );
    });
  })();
  function selectFamily(id) {
    famSel = id;
    var f = FAMS.filter(function (x) {
      return x.id === id;
    })[0];
    $$('.row', fam).forEach(function (g) {
      g.classList.toggle('on', g.getAttribute('data-fam') === id);
      g.setAttribute('aria-pressed', g.getAttribute('data-fam') === id ? 'true' : 'false');
    });
    $('#famcard').innerHTML =
      '<h4>' +
      f.name +
      '</h4><p class="sub">' +
      (f.subHtml || f.sub) +
      '</p><dl><dt>Fired at</dt><dd>' +
      f.fired +
      '</dd><dt>Water</dt><dd>' +
      f.water +
      '</dd><dt>Heat</dt><dd>' +
      f.heat +
      '</dd><dt>You’ll see it as</dt><dd>' +
      f.ex +
      '</dd></dl>';
  }
  $$('.row', fam).forEach(function (g) {
    var go = function () {
      selectFamily(g.getAttribute('data-fam'));
    };
    g.addEventListener('click', go);
    g.addEventListener('keydown', function (e) {
      if (e.key === 'Enter' || e.key === ' ') {
        e.preventDefault();
        go();
      }
    });
  });
  $('#famtable').innerHTML = FAMS.map(function (f) {
    return (
      '<tr><td><b>' +
      f.name +
      '</b><br>' +
      (f.subHtml || f.sub) +
      '</td><td>' +
      f.fired +
      '</td><td>' +
      f.water +
      '</td><td>' +
      f.heat +
      '</td><td>' +
      f.ex +
      '</td></tr>'
    );
  }).join('');

  /* ================= plate 3: heat ================= */
  var HEAT = {
    k: {
      unit: 'W/(m·K)',
      max: 200,
      zmax: 5,
      what: '<b>Thermal conductivity:</b> how fast heat travels through the wall. High numbers spread a burner’s hot spot out; low numbers keep it where it lands.',
      rows: [
        {
          name: 'Aluminum 3003',
          sub: 'non-stick pans and inserts',
          lo: 159,
          hi: 190,
          color: '#5F6772',
          val: '159–190',
        },
        { name: 'Gray cast iron', sub: '', lo: 40, hi: 72, color: '#383D44', val: '40–72' },
        { name: 'Glazed stoneware, porcelain', sub: '', lo: 1, hi: 4, color: '#1B5674', val: '1.0–4.0' },
        { name: 'Unglazed Zisha', sub: 'single source', lo: 1.3, hi: 1.3, color: '#6E3B36', val: '1.3', single: true },
        { name: 'Unglazed terracotta', sub: '', lo: 0.5, hi: 1.3, color: '#B8532F', val: '0.50–1.30' },
      ],
    },
    cv: {
      unit: 'MJ/(m³·K)',
      max: 4,
      zmax: null,
      what: '<b>Volumetric heat capacity:</b> how much heat a given volume of wall stores for each degree. This is what keeps a pan from crashing when cold food lands in it.',
      rows: [
        { name: 'Aluminum', sub: '', lo: 2.4, hi: 2.46, color: '#5F6772', val: '2.40–2.46' },
        { name: 'Gray cast iron', sub: '', lo: 3.27, hi: 3.69, color: '#383D44', val: '3.27–3.69' },
        { name: 'Glazed stoneware, porcelain', sub: '', lo: 1.6, hi: 2.3, color: '#1B5674', val: '1.6–2.3' },
        { name: 'Unglazed Zisha', sub: '', gap: true, val: 'not published', gapText: 'not published' },
        { name: 'Unglazed terracotta', sub: '', lo: 1.2, hi: 1.9, color: '#B8532F', val: '1.2–1.9' },
      ],
    },
    a: {
      unit: 'mm²/s',
      max: 80,
      zmax: 2,
      what: '<b>Thermal diffusivity:</b> how fast a change in temperature sweeps across the wall, which is conductivity divided by stored heat. It’s why aluminum evens out about a hundred times faster than terracotta.',
      rows: [
        { name: 'Aluminum 3003', sub: '', lo: 63, hi: 77, color: '#5F6772', val: '63–77' },
        { name: 'Gray cast iron', sub: '', lo: 10, hi: 18, color: '#383D44', val: '10–18' },
        { name: 'Glazed stoneware, porcelain', sub: '', lo: 0.5, hi: 1.5, color: '#1B5674', val: '0.5–1.5' },
        { name: 'Unglazed Zisha', sub: '', gap: true, val: 'not published', gapText: 'not published' },
        { name: 'Unglazed terracotta', sub: '', lo: 0.2, hi: 0.7, color: '#B8532F', val: '0.2–0.7' },
      ],
    },
  };
  var heatKey = 'k',
    zoom = false;
  var heatBtns = $$('[data-heat]'),
    zoomBtn = $('[data-zoom]');
  function renderHeat() {
    var d = HEAT[heatKey];
    var max = zoom && d.zmax ? d.zmax : d.max;
    zoomBtn.disabled = !d.zmax;
    zoomBtn.style.opacity = d.zmax ? '1' : '.4';
    if (!d.zmax) {
      zoom = false;
      zoomBtn.setAttribute('aria-pressed', 'false');
    }
    $('#heatwhat').innerHTML = d.what + c(12);
    renderBars(
      $('#heatbars'),
      d.rows.map(function (r) {
        var o = {};
        for (var k in r) o[k] = r[k];
        o.val = r.val + (r.gap ? '' : ' ' + d.unit);
        return o;
      }),
      max
    );
    ticks($('#heataxis'), max, d.unit);
    $('#heatcap').innerHTML = zoom
      ? 'Zoomed in to 0–' + max + ' ' + d.unit + ': the metals run off the right edge, which is the point.'
      : heatKey === 'cv'
        ? 'Cast iron stores the most heat per volume, despite having half of aluminum’s heat capacity per kilogram, because it’s so dense.'
        : 'At this scale the clays are slivers; zoom in to tell them apart.';
    if (heatKey === 'k') $('#heatcap').innerHTML += ' Zisha’s 1.3 comes from a single modeling study.' + c(13);
  }
  heatBtns.forEach(function (b) {
    b.addEventListener('click', function () {
      heatKey = b.dataset.heat;
      press(heatBtns, b);
      renderHeat();
    });
  });
  zoomBtn.addEventListener('click', function () {
    if (!HEAT[heatKey].zmax) return;
    zoom = !zoom;
    zoomBtn.setAttribute('aria-pressed', zoom ? 'true' : 'false');
    renderHeat();
  });

  var ovenIn = $('#ovenin');
  function renderOven() {
    var f = +ovenIn.value,
      clay = Math.min(500, f + 100);
    $('#ovenout').textContent = f + '°F';
    $('#ovmetal').textContent = f + '°F';
    $('#ovmetalc').textContent = fToC(f) + '°C · recipe time';
    $('#ovclay').textContent = clay + '°F';
    $('#ovclayc').textContent = fToC(clay) + '°C · 30 min less';
    $('#ovennote').innerHTML =
      (f + 100 > 500 ? 'Capped at 500°F, the most Römertopf allows (250°C). ' : '') +
      'Rule from the US Römertopf booklet: +100°F and 30 minutes less than the recipe, from a cold oven.' +
      c(14);
  }
  ovenIn.addEventListener('input', renderOven);

  /* ================= plate 4: hours ================= */
  var ST = {
    ok: ['c-ok', 'No top-up'],
    done: ['c-done', 'Done early'],
    check: ['c-amb', 'Check it'],
    topup: ['c-amb', 'Top up, warm'],
    not: ['c-bad', 'Not suited'],
    na: ['c-na', 'Not covered'],
  };
  var HRS = [
    {
      name: 'Glazed slow-cooker crock',
      sub: 'glazed stoneware, electric',
      cite: c(15),
      h: {
        2: ['ok', 'No need to add water unless you started dry; it’s barely at a full simmer yet.'],
        4: [
          'ok',
          'Don’t top up: the closed lid loses next to nothing, and every peek costs 20–30 minutes of recovery.',
        ],
        8: [
          'ok',
          'Settles at 185–200°F; the meat has given up 20–40% of its weight in water, which is why you started with 30–50% less broth.',
        ],
      },
    },
    {
      name: 'VitaClay VM7900 / VF7700',
      sub: 'unglazed Zisha, double lid',
      cite: c(17),
      h: {
        2: ['done', 'An 8-hour slow-cooker recipe finishes around here on Stew, with minimal loss.'],
        4: ['check', 'Already past a normal Stew cycle: switch to Warm rather than boiling it dry.'],
        8: ['na', 'The manuals don’t go here: recipes are done hours earlier.'],
      },
    },
    {
      name: 'VitaClay VM7800',
      sub: 'unglazed Zisha, dome-lid stockpot',
      cite: c(17),
      h: {
        2: ['topup', 'Vents like a stockpot: broths over an hour start with 4–8 cups of liquid.'],
        4: ['topup', 'Watch the level, and top up with warm or room-temperature water only.'],
        8: ['topup', 'Periodic warm top-ups; never pour cold water into a hot Zisha pot.'],
      },
    },
    {
      name: 'Soaked Römertopf',
      sub: 'unglazed terracotta, in the oven',
      cite: c(14),
      h: {
        2: ['ok', 'The sweet spot: the walls are still steaming; uncover for the last 15–20 minutes to brown.'],
        4: ['check', 'The soak water is running out; don’t add cold liquid to hot clay.'],
        8: ['not', 'Not suited: the walls dry out early; use a lidded slow cooker or a sealed Dutch oven.'],
      },
    },
    {
      name: 'Enameled cast-iron Dutch oven',
      sub: 'lidded, 250–325°F',
      cite: c(18, 15),
      h: {
        2: ['ok', 'Tight lid, little loss: plenty of liquid left.'],
        4: [
          'check',
          'Check at 3–4 hours, especially above 300°F or with the lid ajar; add ½–1 cup of hot liquid if it’s low.',
        ],
        8: ['topup', 'Keep checking and topping up with hot liquid so it doesn’t scorch.'],
      },
    },
  ];
  var hr = '4',
    hrBtns = $$('[data-hr]');
  function chip(k) {
    return '<span class="chip ' + ST[k][0] + '">' + ST[k][1] + '</span>';
  }
  function renderHrs() {
    $('#hrrows').innerHTML = HRS.map(function (r) {
      var v = r.h[hr];
      return (
        '<div class="hr-row' +
        (reduce ? '' : ' flash') +
        '"><div><b>' +
        r.name +
        '</b><small>' +
        r.sub +
        '</small></div>' +
        chip(v[0]) +
        '<p>' +
        v[1] +
        r.cite +
        '</p></div>'
      );
    }).join('');
  }
  hrBtns.forEach(function (b) {
    b.addEventListener('click', function () {
      hr = b.dataset.hr;
      press(hrBtns, b);
      renderHrs();
    });
  });
  $('#hrtable').innerHTML = HRS.map(function (r) {
    return (
      '<tr><td><b>' +
      r.name +
      '</b><br>' +
      r.sub +
      '</td>' +
      ['2', '4', '8']
        .map(function (k) {
          return '<td>' + ST[r.h[k][0]][1] + ': ' + r.h[k][1] + '</td>';
        })
        .join('') +
      '</tr>'
    );
  }).join('');

  /* ================= plate 5: thermal shock ================= */
  var MATS = {
    earth: { name: 'plain earthenware', pot: '#B8532F', rim: '#8E3B1E' },
    stone: { name: 'commercial stoneware', pot: '#C9C0B3', rim: '#8F877C' },
    zisha: { name: 'Zisha', pot: '#7A4038', rim: '#552A25' },
    cord: { name: 'cordierite flameware', pot: '#D8D0C2', rim: '#9E968A' },
    las: { name: 'petalite (LAS) flameware', pot: '#EFEBE4', rim: '#B4ADA2' },
  };
  function judge(m, dt) {
    if (dt === 0) return ['ok', 'No jump', 'Nothing happens without a temperature difference.'];
    if (m === 'earth')
      return dt >= 100
        ? [
            'bad',
            'Cracks',
            'Past 100°C: plain earthenware fails a water-quench test somewhere below that. This is the wet-pot-into-a-hot-oven mistake.',
          ]
        : [
            'amb',
            'Risky',
            'Plain earthenware fails a water quench somewhere under 100°C, so even this jump is a gamble; ceramic tiles survive cycling at about 130°C.',
          ];
    if (m === 'stone')
      return dt < 100
        ? ['ok', 'Holds', 'Under the 100–150°C range where commercial stoneware fails.']
        : dt <= 150
          ? [
              'amb',
              'May crack',
              'Inside commercial stoneware’s published failure range of 100–150°C (dense lab samples reach 150–250°C).',
            ]
          : ['bad', 'Cracks', 'Past commercial stoneware’s 100–150°C range; only dense lab samples last to 150–250°C.'];
    if (m === 'zisha')
      return dt <= 160
        ? [
            'ok',
            'Passes the standard',
            'China’s GB/T 10816 requires Zisha to survive 180°C into 20°C water, a 160°C jump (the 2008 version used 180°C).',
          ]
        : [
            'amb',
            'Untested',
            'Beyond what Zisha’s national standard tests (160°C); no breaking point has been published, and its thermal expansion is unverified.',
          ];
    if (m === 'cord')
      return dt < 300
        ? ['ok', 'Holds', 'Under cordierite flameware’s 300–650°C failure range.']
        : dt <= 650
          ? ['amb', 'May crack', 'Inside cordierite flameware’s 300–650°C range.']
          : ['bad', 'Cracks', 'Past cordierite flameware’s 300–650°C range.'];
    return dt < 500
      ? ['ok', 'Holds', 'Under petalite flameware’s 500–800°C range; Pyroceram 9608 is rated around 700°C.']
      : ['amb', 'May crack', 'Inside petalite flameware’s 500–800°C range; Pyroceram 9608 is rated around 700°C.'];
  }
  var mat = 'earth',
    matBtns = $$('[data-mat]'),
    dtIn = $('#dt'),
    pot = $('#potsvg');
  function renderShock(animate) {
    var dt = +dtIn.value,
      m = MATS[mat],
      j = judge(mat, dt);
    $('#dtout').textContent = dt + '°C (' + Math.round(dt * 1.8) + '°F)';
    var v = $('#dtverdict');
    v.className = 'verdict-big ' + j[0];
    v.textContent = j[1];
    $('#dtread').innerHTML = '<b>' + dt + '°C jump, ' + m.name + '.</b> ' + j[2] + c(21, 4, 23);
    var anim = animate && !reduce;
    pot.innerHTML = '';
    el('title', { id: 'pottitle' }, pot).textContent =
      'A ' + m.name + ' pot quenched after a ' + dt + '°C jump: ' + j[1];
    // water bath
    el('rect', { x: 40, y: 214, width: 360, height: 70, fill: '#2B6F96', opacity: 0.55 }, pot);
    el(
      'path',
      {
        d: 'M40 214 q20 -6 40 0 t40 0 t40 0 t40 0 t40 0 t40 0 t40 0 t40 0 t40 0',
        stroke: '#9CC7DD',
        'stroke-width': 2,
        fill: 'none',
      },
      pot
    );
    el('text', { x: 48, y: 274, 'font-size': 12, fill: '#FBF4E8', 'font-weight': 600 }, pot).textContent =
      'room-temperature water';
    var g = el('g', {}, pot);
    if (anim) {
      g.style.animation = 'drop .7s cubic-bezier(.5,0,.9,.6) both';
    }
    // heat glow proportional to dt
    var glow = Math.min(1, dt / 800);
    el('ellipse', { cx: 220, cy: 150, rx: 150, ry: 92, fill: '#F2A65A', opacity: (0.08 + glow * 0.35).toFixed(2) }, g);
    var left = el('g', {}, g),
      right = el('g', {}, g);
    var body = 'M110 70 H330 Q336 70 334 80 L318 196 Q314 214 296 214 H144 Q126 214 122 196 L106 80 Q104 70 110 70 Z';
    var clipL = el('clipPath', { id: 'cl' }, pot),
      clipR = el('clipPath', { id: 'cr' }, pot);
    el('polygon', { points: '0 0 222 0 222 62 214 100 230 132 216 166 228 220 228 300 0 300' }, clipL);
    el('polygon', { points: '222 0 440 0 440 300 228 300 228 220 216 166 230 132 214 100 222 62' }, clipR);
    var split = j[0] === 'bad';
    [left, right].forEach(function (half, i) {
      if (split) half.setAttribute('clip-path', i ? 'url(#cr)' : 'url(#cl)');
      el('path', { d: body, fill: m.pot, stroke: m.rim, 'stroke-width': 3 }, half);
      el('rect', { x: 104, y: 64, width: 232, height: 12, rx: 3, fill: m.rim }, half);
      el(
        'path',
        { d: 'M128 100 Q130 160 142 196', stroke: '#FFFFFF', 'stroke-opacity': 0.35, 'stroke-width': 5, fill: 'none' },
        half
      );
    });
    if (split) {
      if (anim) {
        right.style.transition = 'transform .5s ease-out 1.4s';
        right.style.transform = 'translate(0,0)';
        requestAnimationFrame(function () {
          requestAnimationFrame(function () {
            right.style.transform = 'translate(10px,6px) rotate(2deg)';
          });
        });
      } else right.setAttribute('transform', 'translate(10 6) rotate(2 300 140)');
      var cr = el(
        'path',
        {
          d: 'M222 62 L214 100 L230 132 L216 166 L228 214',
          stroke: '#1C1916',
          'stroke-width': 3,
          fill: 'none',
          'stroke-linejoin': 'round',
        },
        g
      );
      if (anim) {
        cr.setAttribute('class', 'fx-draw');
        cr.style.animationDelay = '.7s';
      }
    } else if (j[0] === 'amb') {
      var hl = el(
        'path',
        {
          d: 'M214 214 L222 190 L212 172 L220 154',
          stroke: '#1C1916',
          'stroke-width': 2,
          'stroke-dasharray': '5 4',
          fill: 'none',
        },
        g
      );
      if (anim) {
        hl.setAttribute('class', 'fx-fade');
        hl.style.animationDelay = '.7s';
      }
    } else if (dt > 0) {
      var ok = el(
        'path',
        { d: 'M200 140 l14 14 l28 -28', stroke: '#1F6040', 'stroke-width': 7, fill: 'none', 'stroke-linecap': 'round' },
        g
      );
      if (anim) {
        ok.setAttribute('class', 'fx-fade');
        ok.style.animationDelay = '.7s';
      }
    }
    // steam lines rising from the bath, scaled to dt
    var n = Math.round(glow * 6);
    for (var i = 0; i < n; i++) {
      el(
        'path',
        {
          d: 'M' + (150 + i * 28) + ' 210 q-6 -14 0 -26 t0 -26',
          stroke: '#FBF4E8',
          'stroke-opacity': 0.55,
          'stroke-width': 2,
          fill: 'none',
        },
        pot
      );
    }
  }
  matBtns.forEach(function (b) {
    b.addEventListener('click', function () {
      mat = b.dataset.mat;
      press(matBtns, b);
      renderShock(true);
    });
  });
  dtIn.addEventListener('input', function () {
    renderShock(false);
  });
  dtIn.addEventListener('change', function () {
    renderShock(true);
  });
  $$('[data-dt]').forEach(function (b) {
    b.addEventListener('click', function () {
      dtIn.value = b.dataset.dt;
      renderShock(true);
    });
  });

  renderBars(
    $('#shockbars'),
    [
      {
        name: 'Petalite (LAS) flameware',
        sub: 'Pyroceram 9608 rated ~700°C',
        lo: 500,
        hi: 800,
        color: '#8FD3A8',
        val: '500–800°C',
      },
      { name: 'Cordierite flameware', sub: '', lo: 300, hi: 650, color: '#9CC7DD', val: '300–650°C' },
      {
        name: 'Zisha',
        sub: 'the jump its standard requires it to pass',
        lo: 160,
        hi: 160,
        color: '#D99A90',
        val: 'passes 160°C',
      },
      {
        name: 'Commercial stoneware',
        sub: 'dense lab samples 150–250°C',
        lo: 100,
        hi: 150,
        color: '#CFC6B6',
        val: '100–150°C',
      },
      { name: 'Plain earthenware', sub: 'terracotta', lo: 0, hi: 100, color: '#E08A63', val: 'under 100°C' },
    ],
    800
  );

  /* ================= plate 6: stovetops ================= */
  var STOVE = [
    {
      pot: 'rt',
      name: 'Römertopf',
      sub: 'unglazed terracotta',
      cite: c(14),
      s: {
        gas: ['c-bad', 'No', 'Oven only: a burner’s hot spot snaps the wall.'],
        coil: ['c-bad', 'No', 'The coil’s ring of contact is a severe hot spot.'],
        glass: ['c-bad', 'No', 'Thermal shock, and the grit scratches glass.'],
        ind: ['c-bad', 'No', 'Clay doesn’t couple, and a plate’s hot spots crack it.'],
      },
    },
    {
      pot: 'lc',
      name: 'La Chamba',
      sub: 'burnished, unglazed',
      cite: c(11, 24),
      s: {
        gas: ['c-ok', 'Yes, low', 'Start on low with liquid inside, after the first-use oven cure.'],
        coil: ['c-amb', 'Diffuser', 'Importers and Paula Wolfert say to use a flat diffuser against hot spots.'],
        glass: ['c-amb', 'Diffuser', 'Use a diffuser, and lift it: never slide unglazed clay across glass.'],
        ind: ['c-bad', 'Contested', 'Importers list steel plates on low; Miele and Bosch prohibit them.'],
      },
    },
    {
      pot: 'vc',
      name: 'VitaClay',
      sub: 'unglazed Zisha insert',
      cite: c(17),
      s: {
        gas: ['c-bad', 'Prohibited', 'The manual allows its electric base only.'],
        coil: ['c-bad', 'Prohibited', 'Electric base only.'],
        glass: ['c-bad', 'Prohibited', 'Electric base only.'],
        ind: ['c-bad', 'Prohibited', 'Electric base only, and clay doesn’t couple anyway.'],
      },
    },
    {
      pot: 'mg',
      name: 'Magnifique',
      sub: 'glazed kaolin insert',
      cite: c(7, 24),
      s: {
        gas: ['c-ok', 'Rated', 'Rated for gas stovetops, and the oven up to 750°F.'],
        coil: ['c-ok', 'Rated', 'Rated for electric ranges; heat it gradually.'],
        glass: ['c-amb', 'Careful', 'Ramp up gradually and don’t slide it.'],
        ind: ['c-bad', 'No', 'No iron in it, and cooktop makers warn against plates.'],
      },
    },
    {
      pot: 'al',
      name: 'Aluminum insert',
      sub: 'Ninja MC1001 pot',
      cite: c(28),
      s: {
        gas: ['c-bad', 'No', 'The manual says it isn’t stovetop-safe (oven to 500°F is fine).'],
        coil: ['c-bad', 'No', 'Not stovetop-safe.'],
        glass: ['c-bad', 'No', 'Not stovetop-safe.'],
        ind: ['c-bad', 'No', 'Not stovetop-safe.'],
      },
    },
    {
      pot: 'ci',
      name: 'Cast-iron insert',
      sub: 'enameled gray iron',
      cite: c(29),
      s: {
        gas: ['c-ok', 'Yes', 'Preheat gradually to protect the enamel.'],
        coil: ['c-ok', 'Yes', 'The heavy flat base handles coils.'],
        glass: ['c-ok', 'Yes', 'Lift it rather than sliding it.'],
        ind: ['c-ok', 'Native', 'Iron is magnetic: no plate needed.'],
      },
    },
  ];
  var stove = 'gas',
    stoveBtns = $$('[data-stove]');
  function renderStove() {
    var host = $('#stoverows');
    if (!host) return;
    host.innerHTML = STOVE.map(function (r) {
      var v = r.s[stove];
      return (
        '<div class="stove-row' +
        (r.pot === current ? ' mine' : '') +
        '"><svg aria-hidden="true"><use href="#i-' +
        r.pot +
        '"/></svg><b>' +
        r.name +
        '<br><small style="font-weight:400;color:var(--muted)">' +
        r.sub +
        '</small></b><span class="chip ' +
        v[0] +
        '">' +
        v[1] +
        '</span><p>' +
        v[2] +
        r.cite +
        '</p></div>'
      );
    }).join('');
  }
  stoveBtns.forEach(function (b) {
    b.addEventListener('click', function () {
      stove = b.dataset.stove;
      press(stoveBtns, b);
      renderStove();
    });
  });
  $('#stovetable').innerHTML = STOVE.map(function (r) {
    return (
      '<tr><td><b>' +
      r.name +
      '</b></td>' +
      ['gas', 'coil', 'glass', 'ind']
        .map(function (k) {
          return '<td>' + r.s[k][1] + ': ' + r.s[k][2] + '</td>';
        })
        .join('') +
      '</tr>'
    );
  }).join('');

  /* ================= plate 7: browning map ================= */
  var map = $('#mapsvg');
  var MX0 = 64,
    MX1 = 548,
    MY0 = 16,
    MY1 = 330,
    TMIN = 90,
    TMAX = 360,
    AMIN = 0.15,
    AMAX = 1;
  function mx(t) {
    return MX0 + ((t - TMIN) / (TMAX - TMIN)) * (MX1 - MX0);
  }
  function my(a) {
    return MY1 - ((a - AMIN) / (AMAX - AMIN)) * (MY1 - MY0);
  }
  var dot;
  (function drawMap() {
    el('rect', { x: MX0, y: MY0, width: MX1 - MX0, height: MY1 - MY0, fill: '#FFFCF6', stroke: '#1C1916' }, map);
    el('rect', { x: MX0, y: MY0, width: MX1 - MX0, height: my(0.85) - MY0, fill: '#DCEAF1' }, map);
    el('rect', { x: MX0, y: my(0.3), width: MX1 - MX0, height: MY1 - my(0.3), fill: '#EEE4D2' }, map);
    var defs = el('defs', {}, map);
    var lg = el('linearGradient', { id: 'charg', x1: 0, x2: 1, y1: 0, y2: 0 }, defs);
    el('stop', { offset: 0, 'stop-color': '#6B3A1E', 'stop-opacity': 0 }, lg);
    el('stop', { offset: 1, 'stop-color': '#6B3A1E', 'stop-opacity': 0.28 }, lg);
    el('rect', { x: mx(176), y: MY0, width: mx(200) - mx(176), height: MY1 - MY0, fill: 'url(#charg)' }, map);
    el('rect', { x: mx(200), y: MY0, width: MX1 - mx(200), height: MY1 - MY0, fill: '#6B3A1E', opacity: 0.28 }, map);
    el(
      'rect',
      { x: mx(140), y: my(0.85), width: mx(165) - mx(140), height: my(0.55) - my(0.85), fill: '#E9B86A' },
      map
    );
    el('rect', { x: mx(140), y: my(0.7), width: mx(165) - mx(140), height: my(0.6) - my(0.7), fill: '#C98A16' }, map);
    [
      [100, '#2B6F96', '100°C: wet food sits here'],
      [260, '#861E10', '260°C: PTFE starts to break down'],
      [350, '#861E10', '350°C: fume fever'],
    ].forEach(function (L) {
      el(
        'line',
        { x1: mx(L[0]), x2: mx(L[0]), y1: MY0, y2: MY1, stroke: L[1], 'stroke-width': 2, 'stroke-dasharray': '5 4' },
        map
      );
      var t = el(
        'text',
        {
          x: mx(L[0]) + 4,
          y: L[0] === 350 ? MY0 + 14 : L[0] === 260 ? MY0 + 30 : my(0.8),
          'font-size': 11.5,
          fill: L[1],
          'font-weight': 700,
        },
        map
      );
      t.textContent = L[2];
      if (L[0] !== 100) {
        t.setAttribute('text-anchor', 'end');
        t.setAttribute('x', mx(L[0]) - 4);
      }
    });
    var lab = function (x, y, s, col, anchor) {
      var t = el(
        'text',
        { x: x, y: y, 'font-size': 12, fill: col || '#1C1916', 'font-weight': 700, 'text-anchor': anchor || 'start' },
        map
      );
      t.textContent = s;
      return t;
    };
    lab(mx(152.5), my(0.55) + 16, 'fast browning', '#87500A', 'middle');
    lab(mx(230), MY1 - 40, 'charring from 176–200°C', '#5A2F16', 'middle');
    lab(MX0 + 8, MY0 + 50, 'too wet: the surface steams', '#1B5674');
    lab(MX0 + 8, MY1 - 24, 'too dry: browning slows', '#4E463E');
    for (var t = 100; t <= 350; t += 50) {
      el(
        'text',
        { x: mx(t), y: MY1 + 18, 'text-anchor': 'middle', 'font-size': 12, fill: '#4E463E' },
        map
      ).textContent = t + '°C';
    }
    el(
      'text',
      {
        x: (MX0 + MX1) / 2,
        y: MY1 + 40,
        'text-anchor': 'middle',
        'font-size': 12.5,
        'font-weight': 700,
        fill: '#1C1916',
      },
      map
    ).textContent = 'pan surface temperature →';
    [0.2, 0.4, 0.6, 0.8, 1.0].forEach(function (a) {
      el(
        'text',
        { x: MX0 - 8, y: my(a) + 4, 'text-anchor': 'end', 'font-size': 12, fill: '#4E463E' },
        map
      ).textContent = a.toFixed(1);
    });
    var yl = el(
      'text',
      {
        x: 14,
        y: (MY0 + MY1) / 2,
        'text-anchor': 'middle',
        'font-size': 12.5,
        'font-weight': 700,
        fill: '#1C1916',
        transform: 'rotate(-90 14 ' + (MY0 + MY1) / 2 + ')',
      },
      map
    );
    yl.textContent = 'wetter →  (water activity)';
    dot = el('g', { class: 'dot' }, map);
    el('circle', { r: 13, fill: '#1C1916', opacity: 0.15 }, dot);
    el('circle', { r: 8, fill: '#FFFCF6', stroke: '#1C1916', 'stroke-width': 3 }, dot);
  })();
  var mt = $('#mt'),
    maw = $('#maw');
  function renderMap() {
    var t = +mt.value,
      a = +maw.value;
    dot.setAttribute('transform', 'translate(' + mx(t).toFixed(1) + ' ' + my(a).toFixed(1) + ')');
    $('#mtout').textContent = t + '°C (' + Math.round((t * 9) / 5 + 32) + '°F)';
    $('#mawout').textContent = a.toFixed(2);
    var msg;
    if (t >= 350)
      msg =
        '<b>Fume-fever territory.</b> Around 350°C, overheated PTFE gives off fumes that cause polymer fume fever; this is cast-iron or flameware heat only.';
    else if (t >= 250)
      msg =
        '<b>Too hot for coatings.</b> PTFE starts to deteriorate at 260°C (500°F) and sol-gel ceramic coatings lose their release at 250–300°C; and the food is charring.';
    else if (t > 176 && a <= 0.85) msg = '<b>Charring.</b> Above about 176–200°C, browning turns into burning.';
    else if (a > 0.85)
      msg =
        '<b>Too wet: it steams.</b> Free water on the surface dilutes the reaction and holds the food near 100°C (212°F) until it boils off; this is a lidded clay pot, and why you uncover it at the end.';
    else if (t < 140)
      msg =
        '<b>Below the fast window.</b> Browning still happens slowly near 100°C over long cooks, but a crust needs 140–165°C.';
    else if (a < 0.3)
      msg =
        '<b>Too dry.</b> Below about 0.3, the sugars and amino acids can’t move enough to react, and browning slows despite the heat.';
    else if (t <= 165 && a >= 0.55)
      msg =
        '<b>Fast browning' +
        (a >= 0.6 && a <= 0.7 ? ', right at the peak' : '') +
        '.</b> 140–165°C with a water activity of 0.55–0.85 (peaking at 0.6–0.7) is where crust and aroma come fastest.';
    else if (t <= 165)
      msg =
        '<b>Browning, a bit dry.</b> The temperature’s right, but the surface is drier than the 0.55–0.85 sweet spot.';
    else
      msg =
        '<b>Hot and getting close to charring.</b> Above the fast window of 140–165°C; charring starts around 176–200°C.';
    $('#mapread').innerHTML = msg + c(25, 26);
  }
  [mt, maw].forEach(function (i) {
    i.addEventListener('input', renderMap);
  });
  (function drag() {
    var on = false;
    function at(e) {
      var r = map.getBoundingClientRect();
      var px = ((e.clientX - r.left) / r.width) * 560,
        py = ((e.clientY - r.top) / r.height) * 380;
      var t = TMIN + ((px - MX0) / (MX1 - MX0)) * (TMAX - TMIN);
      var a = AMIN + ((MY1 - py) / (MY1 - MY0)) * (AMAX - AMIN);
      mt.value = Math.max(TMIN, Math.min(TMAX, Math.round(t / 5) * 5));
      maw.value = Math.max(AMIN, Math.min(AMAX, Math.round(a / 0.05) * 0.05)).toFixed(2);
      renderMap();
    }
    // touch: tap to place (so a finger can still scroll the chart sideways); mouse/pen: drag
    map.addEventListener('click', function (e) {
      at(e);
    });
    map.addEventListener('pointerdown', function (e) {
      if (e.pointerType === 'touch') return;
      on = true;
      map.setPointerCapture(e.pointerId);
      at(e);
    });
    map.addEventListener('pointermove', function (e) {
      if (on) at(e);
    });
    map.addEventListener('pointerup', function () {
      on = false;
    });
    map.addEventListener('pointercancel', function () {
      on = false;
    });
  })();

  renderBars(
    $('#stickbars'),
    [
      { name: 'PTFE non-stick', sub: '', lo: 18, hi: 25, color: '#5F6772', val: '18–25 mN/m' },
      { name: 'Glazed ceramic', sub: '', lo: 40, hi: 70, color: '#1B5674', val: '40–70+ mN/m' },
      {
        name: 'Bare iron and iron oxides',
        sub: 'before seasoning',
        lo: 400,
        hi: 1300,
        color: '#383D44',
        val: 'over 400–1,300+ mN/m',
      },
    ],
    1300
  );

  (function depth() {
    var d = $('#depthsvg'),
      x0 = 40,
      x1 = 400;
    function dx(um) {
      return x0 + (um / 500) * (x1 - x0);
    }
    el('rect', { x: 0, y: 30, width: x0, height: 56, fill: '#DCEAF1' }, d);
    el(
      'text',
      { x: 20, y: 24, 'text-anchor': 'middle', 'font-size': 11, fill: '#1B5674', 'font-weight': 700 },
      d
    ).textContent = 'food';
    el('rect', { x: x0, y: 30, width: x1 - x0 + 16, height: 56, fill: '#C2603F' }, d);
    el('rect', { x: dx(5), y: 46, width: dx(400) - dx(5), height: 24, fill: '#E9B86A' }, d);
    el(
      'path',
      { d: 'M' + dx(400) + ' 58 h14 m-5 -5 l5 5 l-5 5', stroke: '#E9B86A', 'stroke-width': 2.5, fill: 'none' },
      d
    );
    el(
      'text',
      { x: dx(200), y: 63, 'text-anchor': 'middle', 'font-size': 12.5, 'font-weight': 700, fill: '#1C1916' },
      d
    ).textContent = 'fats reach 5–400+ µm';
    el('text', { x: x0 + 4, y: 24, 'font-size': 11, fill: '#4E463E', 'font-weight': 700 }, d).textContent =
      'unglazed wall →';
    el('line', { x1: x0, x2: x1, y1: 100, y2: 100, stroke: '#1C1916', 'stroke-width': 1.5 }, d);
    for (var u = 0; u <= 500; u += 100) {
      el('line', { x1: dx(u), x2: dx(u), y1: 100, y2: 107, stroke: '#1C1916' }, d);
      el('text', { x: dx(u), y: 122, 'text-anchor': 'middle', 'font-size': 11.5, fill: '#4E463E' }, d).textContent =
        u + ' µm';
    }
    el(
      'text',
      { x: (x0 + x1) / 2, y: 142, 'text-anchor': 'middle', 'font-size': 11.5, fill: '#4E463E' },
      d
    ).textContent = '500 µm = half a millimeter';
  })();

  /* ================= plate 9: lead ================= */
  renderBars(
    $('#leadbars'),
    [
      {
        name: 'EU Directive 84/500/EEC',
        sub: 'cooking ware over 3 L',
        lo: 1.5,
        hi: 1.5,
        color: '#5F6772',
        val: '1.5 mg/L',
      },
      {
        name: 'US FDA CPG 545.450',
        sub: 'large hollowware, 1.1 L and up',
        lo: 1.0,
        hi: 1.0,
        color: '#1B5674',
        val: '1.0 mg/L',
      },
      { name: 'ISO 6486-2', sub: 'cooking ware heated in use', lo: 0.5, hi: 0.5, color: '#1B5674', val: '0.5 mg/L' },
      {
        name: 'California Prop 65',
        sub: 'settlement benchmark, hollowware',
        lo: 0.1,
        hi: 0.1,
        color: '#1F6040',
        val: '0.1 mg/L',
      },
    ],
    1.5
  );

  /* ================= print: open every drill-down ================= */
  var opened = [];
  window.addEventListener('beforeprint', function () {
    opened = $$('details:not([open])');
    opened.forEach(function (d) {
      d.open = true;
    });
  });
  window.addEventListener('afterprint', function () {
    opened.forEach(function (d) {
      d.open = false;
    });
  });

  /* ================= start ================= */
  renderWall();
  renderHeat();
  renderOven();
  renderHrs();
  renderShock(false);
  renderMap();
  setPot(current);
  onScroll();
})();
