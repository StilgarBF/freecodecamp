const express = require('express');
const app = express();

const helmet = require('helmet');

/**
 * The hidePoweredBy middleware removes the X-Powered-By header.
 * This helps to obscure the technology stack of your application,
 * making it slightly harder for attackers to exploit known vulnerabilities.
 * /
app.use(helmet.hidePoweredBy());

/**
 * The frameguard middleware helps to prevent clickjacking attacks
 * by setting the X-Frame-Options header. The 'deny' action ensures
 * that the page cannot be displayed in a frame, iframe, or object.
 * /
app.use(helmet.frameguard({action: 'deny'}));

/**
 * The xssFilter middleware sets the X-XSS-Protection header to enable
 * the browser's built-in XSS filtering. This helps to mitigate
 * cross-site scripting (XSS) attacks.
 * /
app.use(helmet.xssFilter());

/**
 * The noSniff middleware sets the X-Content-Type-Options header to 'nosniff'.
 * This prevents browsers from trying to guess (or "sniff") the MIME type,
 * which can reduce exposure to drive-by download attacks and other vulnerabilities.
 * /
app.use(helmet.noSniff());

/**
 * The ieNoOpen middleware sets the X-Download-Options header to 'noopen'.
 * This is specifically for Internet Explorer and prevents it from executing
 * downloads in the site's context, which can help mitigate certain types
 * of attacks.
 * /
app.use(helmet.ieNoOpen());

/**
 * HTTP Strict Transport Security (HSTS) is a web security policy
 * which helps to protect websites against protocol downgrade
 * attacks and cookie hijacking. If your website can be accessed
 * via HTTPS you can ask user’s browsers to avoid using insecure HTTP.
 * By setting the header Strict-Transport-Security, you tell the
 * browsers to use HTTPS for the future requests in a specified
 * amount of time. This will work for the requests coming after
 * the initial request.
 * /
let ninetyDaysInSeconds = 90*24*60*60;
app.use(helmet.hsts({
  maxAge: ninetyDaysInSeconds,
  force: true
}));

/**
 * To improve performance, most browsers prefetch DNS records for
 * the links in a page. In that way the destination ip is already
 * known when the user clicks on a link. This may lead to over-use
 * of the DNS service (if you own a big website, visited by
 * millions people…), privacy issues (one eavesdropper could infer
 * that you are on a certain page), or page statistics alteration
 * (some links may appear visited even if they are not).
 * If you have high security needs you can disable DNS prefetching,
 * at the cost of a performance penalty.
 * /
app.use(helmet.dnsPrefetchControl());

/**
 * If you are releasing an update for your website, and you want
 * the users to always download the newer version, you can (try to)
 * disable caching on client’s browser. It can be useful in
 * development too. Caching has performance benefits, which you
 * will lose, so only use this option when there is a real need.
 * /
app.use(helmet.noCache());

/**
 * By setting and configuring a Content Security Policy you can
 * prevent the injection of anything unintended into your page.
 * This will protect your app from XSS vulnerabilities, undesired
 * tracking, malicious frames, and much more. CSP works by
 * defining an allowed list of content sources which are trusted.
 * You can configure them for each kind of resource a web page
 * may need (scripts, stylesheets, fonts, frames, media,
 * and so on...).
 * There are multiple directives available, so a website owner
 * can have a granular control. See HTML 5 Rocks, KeyCDN for more
 * details. Unfortunately CSP is unsupported by older browsers.
 * 
 * By default, directives are wide open, so it’s important
 * to set the defaultSrc directive as a fallback. Helmet supports
 * both defaultSrc and default-src naming styles.
 * The fallback applies for most of the unspecified directives.
 * /
app.use(helmet.contentSecurityPolicy({
  directives: {
    defaultSrc: ["'self'"],
    scriptSrc: ["'self'", "trusted-cdn.com"]
  }
}));
*/

const ninetyDaysInSeconds = 90 * 24 * 60 * 60;
app.use(
  helmet({
    hidePoweredBy: true,
    frameguard: { action: 'deny' },
    xssFilter: true,
    noSniff: true,
    ieNoOpen: true,
    hsts: {
      maxAge: ninetyDaysInSeconds,
      force: true,
    },
    dnsPrefetchControl: { allow: false },
    noCache: true,
    contentSecurityPolicy: {
      directives: {
        defaultSrc: ["'self'"],
        scriptSrc: ["'self'", "trusted-cdn.com"],
      },
    },
  })
);

module.exports = app;
const api = require('./server.js');
app.use(express.static('public'));
app.disable('strict-transport-security');
app.use('/_api', api);
app.get("/", function (request, response) {
  response.sendFile(__dirname + '/views/index.html');
});
let port = process.env.PORT || 3000;
app.listen(port, () => {
  console.log(`Your app is listening on port ${port}`);
});
