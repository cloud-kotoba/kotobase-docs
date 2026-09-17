import('@noble/curves/secp256k1.js').then(()=>console.log('noble ok')).catch(e=>console.log('noble missing:',e.message));
