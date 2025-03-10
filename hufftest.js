/**
 * Simple Huffman Encoding for PlantUML text.
 * This is a basic example and may need to be adapted for
 * complex PlantUML input.
 */
class Node {
    constructor(char, freq, left = null, right = null) {
      this.char = char;
      this.freq = freq;
      this.left = left;
      this.right = right;
    }
  }
  
  class HuffmanEncoder {
    constructor(text) {
      this.text = text;
      this.frequencyMap = new Map();
      this.huffmanTree = null;
      this.charCodes = new Map();
      this.encodedText = '';
      this.decodedText = '';
    }
  
    buildFrequencyMap() {
      for (const char of this.text) {
        this.frequencyMap.set(char, (this.frequencyMap.get(char) || 0) + 1);
      }
    }
  
    buildHuffmanTree() {
      const priorityQueue = [];
      for (const [char, freq] of this.frequencyMap) {
        priorityQueue.push(new Node(char, freq));
      }
      priorityQueue.sort((a, b) => a.freq - b.freq);
  
      while (priorityQueue.length > 1) {
        const left = priorityQueue.shift();
        const right = priorityQueue.shift();
        const parent = new Node(null, left.freq + right.freq, left, right);
        priorityQueue.push(parent);
        priorityQueue.sort((a, b) => a.freq - b.freq);
      }
      this.huffmanTree = priorityQueue[0];
    }
  
    generateCharCodes(node, code = '') {
      if (node) {
        if (node.char) {
          this.charCodes.set(node.char, code);
        }
        this.generateCharCodes(node.left, code + '0');
        this.generateCharCodes(node.right, code + '1');
      }
    }
  
    encode() {
      this.buildFrequencyMap();
      this.buildHuffmanTree();
      this.generateCharCodes(this.huffmanTree);
  
      for (const char of this.text) {
        this.encodedText += this.charCodes.get(char);
      }
      return this.encodedText;
    }
  
    decode() {
      let currentNode = this.huffmanTree;
      for (const bit of this.encodedText) {
        if (bit === '0') {
          currentNode = currentNode.left;
        } else {
          currentNode = currentNode.right;
        }
  
        if (currentNode.char) {
          this.decodedText += currentNode.char;
          currentNode = this.huffmanTree;
        }
      }
      return this.decodedText;
    }
  }
  
  function encodePlantUMLForUrl(plantUmlText) {
    function encode64(data) {
      r = "";
      for (i = 0; i < data.length; i += 3) {
        if (i + 2 == data.length) {
          r += append3bytes(data.charCodeAt(i), data.charCodeAt(i + 1), 0);
        } else if (i + 1 == data.length) {
          r += append3bytes(data.charCodeAt(i), 0, 0);
        } else {
          r += append3bytes(data.charCodeAt(i), data.charCodeAt(i + 1), data.charCodeAt(i + 2));
        }
      }
      return r;
    }
    function append3bytes(b1, b2, b3) {
      c1 = b1 >> 2;
      c2 = ((b1 & 0x3) << 4) | (b2 >> 4);
      c3 = ((b2 & 0xF) << 2) | (b3 >> 6);
      c4 = b3 & 0x3F;
      r = "";
      r += encode6bit(c1 & 0x3F);
      r += encode6bit(c2 & 0x3F);
      r += encode6bit(c3 & 0x3F);
      r += encode6bit(c4 & 0x3F);
      return r;
    }
    function encode6bit(b) {
      if (b < 10) {
        return String.fromCharCode(48 + b);
      }
      b -= 10;
      if (b < 26) {
        return String.fromCharCode(65 + b);
      }
      b -= 26;
      if (b < 26) {
        return String.fromCharCode(97 + b);
      }
      b -= 26;
      if (b == 0) {
        return "-";
      }
      if (b == 1) {
        return "_";
      }
      return "?";
    }
    var s = "";
    var z = "";
    z = deflate(plantUmlText);
    s = encode64(z);
    return s;
  }
  
  function deflate(str) {
    var compressed = window.pako.deflateRaw(str);
    var strData = "";
    for (var i = 0; i < compressed.length; i++) {
      strData += String.fromCharCode(compressed[i]);
    }
    return strData;
  }
  async function getHttpStatusCode(encodedPlantUml) {
    const url = `https://www.plantuml.com/plantuml/svg/${encodedPlantUml}`;
    try {
      const response = await fetch(url);
      return response.status;
    } catch (error) {
      console.error("Error fetching URL:", error);
      return null;
    }
  }
  
  // PlantUML Text (provided by you)
  const plantUmlText = `@startuml
  participant Participant as Foo
  actor       Actor       as Foo1
  boundary    Boundary    as Foo2
  control     Control     as Foo3
  entity      Entity      as Foo4
  database    Database    as Foo5
  collections Collections as Foo6
  queue       Queue       as Foo7
  Foo -> Foo1 : To actor
  Foo -> Foo2 : To boundary
  Foo -> Foo3 : To control
  Foo -> Foo4 : To entity
  Foo -> Foo5 : To database
  Foo -> Foo6 : To collections
  Foo -> Foo7: To queue
  @enduml`;
  
  // Example Usage
  (async () => {
    const encoder = new HuffmanEncoder(plantUmlText);
    const encodedData = encoder.encode();
    const encodedUrlData = encodePlantUMLForUrl(plantUmlText)
    console.log(`Encoded String for url: ${encodedData}`)
  
    const plantUmlUrl = `https://www.plantuml.com/plantuml/svg/${encodedUrlData}`;
    console.log(`PlantUML URL: ${plantUmlUrl}`);
    const httpStatusCode = await getHttpStatusCode(encodedUrlData);
    console.log(`HTTP Status Code: ${httpStatusCode}`);
  })();