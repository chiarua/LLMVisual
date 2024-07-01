export class Scorer {
    constructor(type) {
        this.type = type;
        this.scoreIndex = this.initScore();
    }
    getFeatureScore(feature) {
        const type = this.type;
        const score = this.scoreIndex[feature];
        if (score !== undefined) {
            return { type, feature, score };
        }
        return undefined;
    }
}
//# sourceMappingURL=base.js.map