document.getElementById('no').play();



const input = document.querySelector('.input');
      const input2 = document.querySelector('.input2');
      const button = document.querySelector('.button');

      // ясту

      alphabetchoice = ''

      // letters
      alphabet = 'abcdefghijklmnopqrstuvwxyz '
      alphabet2 = 'фджмяьйцнгшщзхъчывапролби火э'
      alphabet3 = 'ㅂㅈㄷㄱ쇼ㅕㅑㅐㅔ]ㅁㄴㅇㄹ호ㅓㅏㅣㅋㅌㅊ퓨ㅜ ㅡみ'
      alphabet4 = 'たていすかんなにらせちとしはきくまのりれけむつさそひこ'
      alphabet5 = 'ςερτυθιοπασδφγηξκλζχψωβνμ¥§'
      console.log(alphabet4.length);

      alphanum = 'юㅒみ€'

      random_num = Math.floor(Math.random() * alphanum.length)

      lang = alphanum.charAt(random_num)
      console.log(lang)

      function tran() {
        let translation = ''; let curr_char = ''
        for (let i = 0; i < input.value.length; i++) {curr_char = input.value.charAt(i); for (var j = 0; j < alphabet.length; j++) {if (curr_char == alphabet.charAt(j)) {translation = translation + alphabet2.charAt(j)}}}
        input.value = translation + lang
      }

      function tran2() {
        let translation = ''; let curr_char = ''
        for (let i = 0; i < input.value.length; i++) {curr_char = input.value.charAt(i); for (var j = 0; j < alphabet.length; j++) {if (curr_char == alphabet.charAt(j)) {translation = translation + alphabet3.charAt(j)}}}
        input.value = translation + lang
      }

      function tran3() {
        let translation = ''; let curr_char = ''
        for (let i = 0; i < input.value.length; i++) {curr_char = input.value.charAt(i); for (var j = 0; j < alphabet.length; j++) {if (curr_char == alphabet.charAt(j)) {translation = translation + alphabet4.charAt(j)}}}
        input.value = translation + lang
      }

      function tran4() {
        let translation = ''; let curr_char = ''
        for (let i = 0; i < input.value.length; i++) {curr_char = input.value.charAt(i); for (var j = 0; j < alphabet.length; j++) {if (curr_char == alphabet.charAt(j)) {translation = translation + alphabet5.charAt(j)}}}
        input.value = translation + lang
      }

      function t() {
        if (lang === alphanum.charAt(0)) {tran()}
        if (lang === alphanum.charAt(1)) {tran2()}
        if (lang === alphanum.charAt(2)) {tran3()}
        if (lang === alphanum.charAt(3)) {tran4()}
      }

      function decode() {
        let translation = ''; let curr_char = ''
        if (input2.value === alphanum.charAt(0)) {alphabetchoice = alphabet2}
        if (input2.value === alphanum.charAt(1)) {alphabetchoice = alphabet3}
        if (input2.value === alphanum.charAt(2)) {alphabetchoice = alphabet4}
        if (input2.value === alphanum.charAt(3)) {alphabetchoice = alphabet5}
        for (let i = 0; i < (input.value.length;-1) i++) {
          curr_char = input.value.charAt(i); for (var j = 0; j < alphabetchoice.length; j++) {
            if (curr_char == alphabetchoice.charAt(j)) {
              translation = translation + alphabet.charAt(j)
            }
          }
        }
        input.value = translation
      }