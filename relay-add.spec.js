/**
 * @author Thomas Bock (Thomas.Bock@ptb.de)
 * version: 2013-01-18
 */
 
var add = require("./relay-add.js");

// Der Text "relay-add.js (Laden & Ausführen):" ist ungünstig, da
// hieraus u.U. ein Dateiname gebildet wird mit üblen Zeichen drin.
// (derzeitiger Stand der Erkenntnis). RN
describe('relay-add loading and execution', function() {
  it('relay-add is available over require', function() {
    expect(add).toBeDefined();
  });
  it('relay-add says Hello World', function() {
    expect(add.helloWorld).toMatch("Hello World");
  });
});

describe('The function _.vlStat():', function() {
  it('- is available over require', function() {
    expect(add.vlStat).toBeDefined();
  });
  it('- gives undefined without param', function() {
    expect(add.vlStat()).toBeUndefined();
  });
  it('- dont calculate anything if fewer than three valves in the array',
  function() {
    expect(add.vlStat([1, 2])).toBeUndefined();
  });
  it('- calculates a correct mean value', function() {
    expect(add.vlStat([2, 2, 2]).mv).toEqual(2);
  });
  it('- calculates a correct standard deviation', function() {
    expect(add.vlStat([2, 2, 2]).sd).toEqual(0);
  });
  it('- counts the correct number of array elements', function() {
    expect(add.vlStat([2, 2, 2]).N).toEqual(3);
  });
});

describe('The function _.checkNumArr():', function() {
  it('- is available over require', function() {
    expect(add.checkNumArr).toBeDefined();
  });
  it('- returns undefined without param', function() {
    expect(add.checkNumArr()).toBeUndefined();
  });
  it('- recognizes wrong values', function() {
    expect(add.checkNumArr([1, "p", "-"]).Arr).toEqual([1]);
  });
  it('gives back the correct skip indeces ', function() {
    expect(add.checkNumArr([1, "p", "-"]).Skip).toEqual([1, 2]);
  });
});

describe('The function _.fm3CalQsp():', function() {
  it('- is available over require', function() {
    expect(add.fm3CalQsp).toBeDefined();
  });
  it('- returns undefined without param', function() {
    expect(add.fm3CalQsp()).toBeUndefined();
  });
  it('- returns undefined with undefined 1st param', function() {
    expect(add.fm3CalQsp(undefined, 1, false)).toBeUndefined();
  });
  it('- returns undefined with undefined 2nd param', function() {
    expect(add.fm3CalQsp(1, undefined, false)).toBeUndefined();
  });
  it('- returns undefined with undefined third param', function() {
    expect(add.fm3CalQsp(1, 2, undefined)).toBeUndefined();
  });
  it('- makes sp1 0 on pist equal psoll ', function() {
    expect(add.fm3CalQsp(1, 1, false).sp1).toEqual(0);
  });
});
