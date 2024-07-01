import { SpecQueryModel } from '../../model';
import { Schema } from '../../schema';
import { QueryConfig } from '../../config';
import { FeatureScore } from '../ranking';
import { Dict } from '../../util';
export declare abstract class Scorer {
    readonly type: string;
    readonly scoreIndex: Dict<number>;
    constructor(type: string);
    protected abstract initScore(): Dict<number>;
    protected getFeatureScore(feature: string): FeatureScore;
    abstract getScore(specM: SpecQueryModel, schema: Schema, opt: QueryConfig): FeatureScore[];
}
