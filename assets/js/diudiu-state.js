(function () {
  const states = ['sit', 'run', 'idle', 'static', 'jump'];
  const durations = {
    sit: 3200,
    run: 1000,
    idle: 3600,
    static: 4500,
    jump: 1500,
  };

  const pickNextState = (current) => {
    if (!states.length) {
      return 'sit';
    }

    if (states.length === 1) {
      return states[0];
    }

    let next = states[Math.floor(Math.random() * states.length)];
    while (next === current) {
      next = states[Math.floor(Math.random() * states.length)];
    }
    return next;
  };

  const getRandomInterval = (state) => {
    const base = durations[state] || 3000;
    const jitter = base * 0.35;
    return base - jitter + Math.random() * jitter * 2;
  };

  const runStateMachine = (pet) => {
    const applyState = (state) => {
      const classes = states.map((s) => `diudiu-state--${s}`);
      pet.classList.remove(...classes);
      pet.classList.add(`diudiu-state--${state}`);
      pet.dataset.diudiuState = state;
    };

    const tick = () => {
      const next = pickNextState(pet.dataset.diudiuState);
      applyState(next);
      const wait = getRandomInterval(next);
      window.setTimeout(tick, wait);
    };

    const fallback = pickNextState(null);
    applyState(fallback);
    window.setTimeout(tick, getRandomInterval(fallback));
  };

  if (document.readyState === 'loading') {
    document.addEventListener('DOMContentLoaded', () => {
      const pet = document.querySelector('.diudiu-pet');
      if (pet) {
        runStateMachine(pet);
      }
    }, { once: true });
  } else {
    const pet = document.querySelector('.diudiu-pet');
    if (pet) {
      runStateMachine(pet);
    }
  }
})();
