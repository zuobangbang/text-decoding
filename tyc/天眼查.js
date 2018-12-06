function(t) {
    "use strict";
    function e(t, e) {
        var i = (65535 & t) + (65535 & e);
        return (t >> 16) + (e >> 16) + (i >> 16) << 16 | 65535 & i
    }
    function i(t, e) {
        return t << e | t >>> 32 - e
    }
    function a(t, a, s, n, c, l) {
        return e(i(e(e(a, t), e(n, l)), c), s)
    }
    function s(t, e, i, s, n, c, l) {
        return a(e & i | ~e & s, t, e, n, c, l)
    }
    function n(t, e, i, s, n, c, l) {
        return a(e & s | i & ~s, t, e, n, c, l)
    }
    function c(t, e, i, s, n, c, l) {
        return a(e ^ i ^ s, t, e, n, c, l)
    }
    function l(t, e, i, s, n, c, l) {
        return a(i ^ (e | ~s), t, e, n, c, l)
    }
    function d(t, i) {
        t[i >> 5] |= 128 << i % 32,
        t[14 + (i + 64 >>> 9 << 4)] = i;
        var a, d, r, o, p, v = 1732584193, m = -271733879, u = -1732584194, h = 271733878;
        for (a = 0; a < t.length; a += 16)
            d = v,
            r = m,
            o = u,
            p = h,
            v = s(v, m, u, h, t[a], 7, -680876936),
            h = s(h, v, m, u, t[a + 1], 12, -389564586),
            u = s(u, h, v, m, t[a + 2], 17, 606105819),
            m = s(m, u, h, v, t[a + 3], 22, -1044525330),
            v = s(v, m, u, h, t[a + 4], 7, -176418897),
            h = s(h, v, m, u, t[a + 5], 12, 1200080426),
            u = s(u, h, v, m, t[a + 6], 17, -1473231341),
            m = s(m, u, h, v, t[a + 7], 22, -45705983),
            v = s(v, m, u, h, t[a + 8], 7, 1770035416),
            h = s(h, v, m, u, t[a + 9], 12, -1958414417),
            u = s(u, h, v, m, t[a + 10], 17, -42063),
            m = s(m, u, h, v, t[a + 11], 22, -1990404162),
            v = s(v, m, u, h, t[a + 12], 7, 1804603682),
            h = s(h, v, m, u, t[a + 13], 12, -40341101),
            u = s(u, h, v, m, t[a + 14], 17, -1502002290),
            m = s(m, u, h, v, t[a + 15], 22, 1236535329),
            v = n(v, m, u, h, t[a + 1], 5, -165796510),
            h = n(h, v, m, u, t[a + 6], 9, -1069501632),
            u = n(u, h, v, m, t[a + 11], 14, 643717713),
            m = n(m, u, h, v, t[a], 20, -373897302),
            v = n(v, m, u, h, t[a + 5], 5, -701558691),
            h = n(h, v, m, u, t[a + 10], 9, 38016083),
            u = n(u, h, v, m, t[a + 15], 14, -660478335),
            m = n(m, u, h, v, t[a + 4], 20, -405537848),
            v = n(v, m, u, h, t[a + 9], 5, 568446438),
            h = n(h, v, m, u, t[a + 14], 9, -1019803690),
            u = n(u, h, v, m, t[a + 3], 14, -187363961),
            m = n(m, u, h, v, t[a + 8], 20, 1163531501),
            v = n(v, m, u, h, t[a + 13], 5, -1444681467),
            h = n(h, v, m, u, t[a + 2], 9, -51403784),
            u = n(u, h, v, m, t[a + 7], 14, 1735328473),
            m = n(m, u, h, v, t[a + 12], 20, -1926607734),
            v = c(v, m, u, h, t[a + 5], 4, -378558),
            h = c(h, v, m, u, t[a + 8], 11, -2022574463),
            u = c(u, h, v, m, t[a + 11], 16, 1839030562),
            m = c(m, u, h, v, t[a + 14], 23, -35309556),
            v = c(v, m, u, h, t[a + 1], 4, -1530992060),
            h = c(h, v, m, u, t[a + 4], 11, 1272893353),
            u = c(u, h, v, m, t[a + 7], 16, -155497632),
            m = c(m, u, h, v, t[a + 10], 23, -1094730640),
            v = c(v, m, u, h, t[a + 13], 4, 681279174),
            h = c(h, v, m, u, t[a], 11, -358537222),
            u = c(u, h, v, m, t[a + 3], 16, -722521979),
            m = c(m, u, h, v, t[a + 6], 23, 76029189),
            v = c(v, m, u, h, t[a + 9], 4, -640364487),
            h = c(h, v, m, u, t[a + 12], 11, -421815835),
            u = c(u, h, v, m, t[a + 15], 16, 530742520),
            m = c(m, u, h, v, t[a + 2], 23, -995338651),
            v = l(v, m, u, h, t[a], 6, -198630844),
            h = l(h, v, m, u, t[a + 7], 10, 1126891415),
            u = l(u, h, v, m, t[a + 14], 15, -1416354905),
            m = l(m, u, h, v, t[a + 5], 21, -57434055),
            v = l(v, m, u, h, t[a + 12], 6, 1700485571),
            h = l(h, v, m, u, t[a + 3], 10, -1894986606),
            u = l(u, h, v, m, t[a + 10], 15, -1051523),
            m = l(m, u, h, v, t[a + 1], 21, -2054922799),
            v = l(v, m, u, h, t[a + 8], 6, 1873313359),
            h = l(h, v, m, u, t[a + 15], 10, -30611744),
            u = l(u, h, v, m, t[a + 6], 15, -1560198380),
            m = l(m, u, h, v, t[a + 13], 21, 1309151649),
            v = l(v, m, u, h, t[a + 4], 6, -145523070),
            h = l(h, v, m, u, t[a + 11], 10, -1120210379),
            u = l(u, h, v, m, t[a + 2], 15, 718787259),
            m = l(m, u, h, v, t[a + 9], 21, -343485551),
            v = e(v, d),
            m = e(m, r),
            u = e(u, o),
            h = e(h, p);
        return [v, m, u, h]
    }
    function r(t) {
        var e, i = "", a = 32 * t.length;
        for (e = 0; e < a; e += 8)
            i += String.fromCharCode(t[e >> 5] >>> e % 32 & 255);
        return i
    }
    function o(t) {
        var e, i = [];
        for (i[(t.length >> 2) - 1] = void 0,
        e = 0; e < i.length; e += 1)
            i[e] = 0;
        var a = 8 * t.length;
        for (e = 0; e < a; e += 8)
            i[e >> 5] |= (255 & t.charCodeAt(e / 8)) << e % 32;
        return i
    }
    function p(t) {
        return r(d(o(t), 8 * t.length))
    }
    function v(t, e) {
        var i, a, s = o(t), n = [], c = [];
        for (n[15] = c[15] = void 0,
        s.length > 16 && (s = d(s, 8 * t.length)),
        i = 0; i < 16; i += 1)
            n[i] = 909522486 ^ s[i],
            c[i] = 1549556828 ^ s[i];
        return a = d(n.concat(o(e)), 512 + 8 * e.length),
        r(d(c.concat(a), 640))
    }
    function m(t) {
        var e, i, a = "0123456789abcdef", s = "";
        for (i = 0; i < t.length; i += 1)
            e = t.charCodeAt(i),
            s += a.charAt(e >>> 4 & 15) + a.charAt(15 & e);
        return s
    }
    function u(t) {
        return unescape(encodeURIComponent(t))
    }
    function h(t) {
        return p(u(t))
    }
    function f(t) {
        return m(h(t))
    }
    function g(t, e) {
        return v(u(t), u(e))
    }
    function b(t, e) {
        return m(g(t, e))
    }
    function y(t, e, i) {
        return e ? i ? g(e, t) : b(e, t) : i ? h(t) : f(t)
    }